# cs2-amd-bb-util
Utility to combat recurring scaling issues with CS2 Black Bars and AMD. This project aims to circumvent any future updates breaking black bars on CS2 for 4:3 resolutions.

## Download
[github](https://github.com/fuglyuckDev/cs2-amd-bb-util/blob/main/dist/AMD%20BB%20Util.exe) -> (Click download raw button in top right of screen)

## How does it work?
This utility is a simple python script that leverages nircmd to change the resolution of your main monitor in windows rather than in game.
Simply open the utility, set your resolution and refresh rate and hit "Launch CS2".

## What's under the hood?
Python is the main driver here, using tkinter for the user interface, screeninfo to get your default screen's resolution on startup, sys, os, tempfile, subprocess to handle creating, writing and reading .bat files created in a temp file in your appdata folder ```C:\Users\user\AppData\Local\tmpabc123```

## Imports used:
- [tkinter](https://docs.python.org/3/library/tkinter.html)
- [screeninfo](https://pypi.org/project/screeninfo/)
- [nircmd](https://www.nirsoft.net/utils/nircmd.html) (Bundled)

## Prerequisites
Make sure you set your windows scaling mode to preserve aspect ratio in AMD Adrenaline:
- Head over to AMD Adrenaline
- click the cog in the top right of the application
- head to the display tab
- select main monitor
- GPU Scaling Enabled
- Scaling mode Preserve aspect ratio

### Notes
- Currently this build is fully manual, so you will have to click "Revert Resolution" to switch back to your old res.
- In this version, make sure to keep the window open while you're playing, as when the application starts up, it will use the resolution you launched the application with to be the resolution you revert back to.
  - (Launching the app with a resolution of 800x600 will cause the revert button to attempt to revert back to 800x600, so **MAKE SURE YOU LAUNCH THE APP USING YOUR DEFAULT RES :)**)
- As this is a simple app with no signature, windows will more than likely throw a fit when trying to launch it. If you're worried about what the code does, have a look at ```AMD BB Util.py```. This is the main python script with partial documentation so you can see what's going on under the hood.
- **THIS ONLY WORKS ON WINDOWS**
