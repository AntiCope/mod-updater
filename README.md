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
    - [updater.py](https://github.com/AntiCope/mod-updater/releases/download/latest/updater.py) if you are using linux *(remember to install dependencies)*
2. Create `updater.json` use schema defined [below](#configuration)


# Configuration
If you are using an [editor that supports json schema](https://json-schema.org/implementations.html), you can start by creating `updater.json` with following contents:
```json
{
    "$schema": "https://raw.githubusercontent.com/AntiCope/mod-updater/master/schema.json"
}
```
This should help you create valid configuration file.

Otherwise read [updater.json](./updater.json) to see an example of how a proprer configuration file should look.

# Command line args:
- `--nogui, -ng` - disable progress bar gui