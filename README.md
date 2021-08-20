<h1 align="center">Minecraft Mod Updater</h1>
<p align="center">
A pretty bad automatic mod updater. Supports direct links, modrinth, github releases and curseforge.
</p>
<div align="center">
    <img src="https://img.shields.io/github/last-commit/AntiCope/mod-updater?logo=git" alt="Last commit">
    <img src="https://img.shields.io/github/workflow/status/AntiCope/mod-updater/PyInstaller%20Build?logo=github" alt="build status">
</div>

# Installation

1. Download:
    - [windows-updater.exe](https://github.com/AntiCope/mod-updater/releases/download/latest/windows-updater.exe) if you are using windows
    - [macos-updater](https://github.com/AntiCope/mod-updater/releases/download/latest/macos-updater) if you are using mac os
    - [updater.py](https://github.com/AntiCope/mod-updater/releases/download/latest/updater.py) if you are using linux *(remember to install [requests](https://pypi.org/project/requests/) and [wxPython](https://wiki.wxpython.org/How%20to%20install%20wxPython))*
2. Create `updater.json`in the same directory as your binary. Use schema defined [below](#configuration)

# Configuration
If you are using an [editor that supports json schema](https://json-schema.org/implementations.html), you can start by creating `updater.json` with following contents:
```json
{
    "$schema": "https://raw.githubusercontent.com/AntiCope/mod-updater/master/schema.json"
}
```
This should help you create valid configuration file. You can also use [this website](https://rjsf-team.github.io/react-jsonschema-form/#eyJmb3JtRGF0YSI6eyJ2ZXJzaW9uIjpbIjEuMTcuMSJdLCJwYXRoIjoiLiIsImRpcmVjdCI6W10sIm1vZHJpbnRoIjpbXSwiZ2l0aHViX3JlbGVhc2VzIjpbXSwiY3Vyc2Vmb3JnZSI6W119LCJzY2hlbWEiOnsidHlwZSI6Im9iamVjdCIsImRlc2NyaXB0aW9uIjoiQ29uZmlnIGZpbGUiLCJwcm9wZXJ0aWVzIjp7InZlcnNpb24iOnsidHlwZSI6ImFycmF5IiwiaXRlbXMiOnsidHlwZSI6InN0cmluZyJ9LCJkZXNjcmlwdGlvbiI6Ik1pbmVjcmFmdCB2ZXJzaW9uIG9yIHZlcnNpb25zLiJ9LCJwYXRoIjp7InR5cGUiOiJzdHJpbmciLCJkZXNjcmlwdGlvbiI6IlBhdGggdG8gLm1pbmVjcmFmdC9tb2RzIn0sImRpcmVjdCI6eyJ0eXBlIjoiYXJyYXkiLCJpdGVtcyI6eyJ0eXBlIjoib2JqZWN0IiwicHJvcGVydGllcyI6eyJuYW1lIjp7IiRyZWYiOiIjL2RlZmluaXRpb25zL25hbWUifSwidXJsIjp7InR5cGUiOiJzdHJpbmciLCJmb3JtYXQiOiJ1cmkifX0sInJlcXVpcmVkIjpbIm5hbWUiLCJ1cmwiXX19LCJtb2RyaW50aCI6eyJ0eXBlIjoiYXJyYXkiLCJpdGVtcyI6eyJ0eXBlIjoib2JqZWN0IiwicHJvcGVydGllcyI6eyJuYW1lIjp7IiRyZWYiOiIjL2RlZmluaXRpb25zL25hbWUifSwiaWQiOnsidHlwZSI6InN0cmluZyJ9fSwicmVxdWlyZWQiOlsibmFtZSIsImlkIl19fSwiZ2l0aHViX3JlbGVhc2VzIjp7InR5cGUiOiJhcnJheSIsIml0ZW1zIjp7InR5cGUiOiJvYmplY3QiLCJwcm9wZXJ0aWVzIjp7Im5hbWUiOnsiJHJlZiI6IiMvZGVmaW5pdGlvbnMvbmFtZSJ9LCJyZXBvIjp7InR5cGUiOiJzdHJpbmciLCJwYXR0ZXJuIjoiW2EtekEtWjAtOS1dezEsNjN9L1thLXpBLVowLTktXXsxLDYzfSJ9fSwicmVxdWlyZWQiOlsibmFtZSIsInJlcG8iXX19LCJjdXJzZWZvcmdlIjp7InR5cGUiOiJhcnJheSIsIml0ZW1zIjp7InR5cGUiOiJvYmplY3QiLCJwcm9wZXJ0aWVzIjp7Im5hbWUiOnsiJHJlZiI6IiMvZGVmaW5pdGlvbnMvbmFtZSJ9LCJpZCI6eyJ0eXBlIjoiaW50ZWdlciJ9fSwicmVxdWlyZWQiOlsibmFtZSIsImlkIl19fX0sImRlZmluaXRpb25zIjp7Im5hbWUiOnsicGF0dGVybiI6IlteXFwvOj8qXCI8PnxdKlxcLmphciIsInR5cGUiOiJzdHJpbmciLCJkZXNjcmlwdGlvbiI6IkZpbGVuYW1lIHlvdSB3YW50IHlvdXIgbW9kIHRvIGJlIHNhdmVkIGFzIn19LCJyZXF1aXJlZCI6WyJ2ZXJzaW9uIiwicGF0aCJdfSwidWlTY2hlbWEiOnt9LCJ0aGVtZSI6ImZsdWVudC11aSIsImxpdmVTZXR0aW5ncyI6eyJ2YWxpZGF0ZSI6dHJ1ZSwiZGlzYWJsZSI6ZmFsc2UsIm9taXRFeHRyYURhdGEiOnRydWUsImxpdmVPbWl0Ijp0cnVlfX0=) to generate updater.json by using a form.

Otherwise read [updater.json](./updater.json) to see an example of how a proprer configuration file should look.

# Command line args:
- `--nogui, -ng` - disable progress bar gui
