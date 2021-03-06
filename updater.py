from json import load
import requests
from threading import Thread
import sys
from os import chdir
from dateutil.parser import isoparse
from time import sleep

try:
    from colorama import init
    init()
except ImportError:
    pass

gui = True
for arg in sys.argv:
    if "headless" in arg:
        gui = False
        break
    if "nogui" in arg:
        gui = False
        break
    if "ng" in arg:
        gui = False
        break
    
if gui:
    import wx

CATEGORY_KEYS = ['direct', 'modrinth', 'github_releases', 'curseforge']
JAR_MIMETYPES = ["application/x-java-archive", "application/java-archive"]

def load_data():
    try:
        data = load(open("updater.json","r", encoding='utf-8')) 
    except Exception as ex:
        print(f"\033[31mCouldn't parse update.json. Error: {ex}\033[0m")
    
    for key in CATEGORY_KEYS+['version']:
        if key not in data.keys():
            print(f"\033[93mWarn: \"{key}\" doesn't exist\033[0m")
            data[key] = []
    
    if isinstance(data['version'], str):
        data['version'] = [data['version']]
        
    if "loader" not in data.keys():
        print(f"\033[93mWarn: \"loader\" doesn't exist\033[0m")
        data['loader'] = 'fabric'
        
    if "path" not in data.keys():
        print(f"\033[93mWarn: \"path\" doesn't exist\033[0m")
        data['path'] = '.'
        
    data['count'] = 0
    for key in CATEGORY_KEYS:
        data['count'] += len(data[key])
        
    return data

data = load_data()

progress = None

chdir(data['path'])

if not gui:
    print("Running without gui")
else:
    app = wx.App()
    progress = wx.ProgressDialog("Downloading mods", "Initializing", data['count'], style=wx.PD_CAN_ABORT | wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME)

completed = 0

def increment():
    global completed
    completed += 1
    if gui:
        try:
            progress.Update(completed)
        except wx.wxAssertionError:
            pass

def update_name(name):
    global completed
    print(f"Downloading: \033[36m{name}\033[0m")
    if gui:
        try:
            progress.Update(completed, newmsg=f"Downloading: {name}")
        except wx.wxAssertionError:
            pass

def download(url, file):
    r = requests.get(url)
    if r.status_code != 200:
        raise requests.HTTPError(f"Status code: {r.status_code}")
    with open(file, "w+b") as fp:
        fp.write(r.content)

def set_intersect(a, b):
    for ai in a:
        if ai in b:
            return ai
    return False

def sort_entries(entry, key):
    return sorted(entry, key=lambda x: isoparse(x[key]), reverse=True)

def download_direct(mod):
    download(mod['url'], mod['name'])

def download_modrinth(mod):
    r = requests.get(f"https://api.modrinth.com/api/v1/mod/{mod['id']}/version")
    r = r.json()
    r = sort_entries(r, 'date_published')
    version = {}
    for ver in r:
        if set_intersect(data['version'], ver['game_versions']) and data['loader'] in ver['loaders']:
            version = ver
            break
    if not version:
        raise KeyError(f"No valid version found: {mod['name']}")
    download(version['files'][0]['url'], mod['name'])
    
def download_github_releases(mod):
    r = requests.get(f"https://api.github.com/repos/{mod['repo']}/releases")
    r = r.json()
    r = sort_entries(r, 'published_at')
    dl = ""
    for release in r:
        for asset in release['assets']:
            if asset['content_type'] in JAR_MIMETYPES:
                dl = asset['browser_download_url']
                break
        else:
            continue
        break
    if not dl:
        raise KeyError(f"No valid release found: {mod['name']}")
    download(dl, mod['name'])
    
def download_curseforge(mod):
    r = requests.get(f"https://addons-ecs.forgesvc.net/api/v2/addon/{mod['id']}/files", headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"})
    r = r.json()
    r = sort_entries(r, 'fileDate')
    dl = ""
    for file in r:
        if set_intersect(data['version'], file['gameVersion']):
            dl = file['downloadUrl']
            break
    if not dl:
        raise KeyError(f"No valid version found: {mod['name']}")
    download(dl, mod['name'])

def download_mods(category, func):
    for mod in data[category]:
        if gui and progress.WasCancelled():
            print(f"\033[93mCancelled\033[0m")
            break
        update_name(mod['name'])
        try:
            func(mod)
        except Exception as ex:
            print(f"\033[31mError: {ex}\033[0m")
        increment()

threads = []
threads.append(Thread(target=download_mods, args=("direct", download_direct, )))
threads.append(Thread(target=download_mods, args=("modrinth", download_modrinth, )))
threads.append(Thread(target=download_mods, args=("github_releases", download_github_releases, )))
threads.append(Thread(target=download_mods, args=("curseforge", download_curseforge, )))

for thread in threads:
    thread.start()
    sleep(0.1)

for thread in threads:
    try:
        thread.join()
    except RuntimeError:
        pass

if gui:
    progress.Destroy()
