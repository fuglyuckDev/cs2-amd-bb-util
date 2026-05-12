import tkinter as tk
from tkinter import ttk
from screeninfo import get_monitors
import sys, os, tempfile, subprocess

# List of common 4:3 resolutions
resolutions = [{ "label": "160x120", "width": 160, "height": 120 },
  { "label": "320x240", "width": 320, "height": 240 },
  { "label": "400x300", "width": 400, "height": 300 },
  { "label": "640x480", "width": 640, "height": 480 },
  { "label": "800x600", "width": 800, "height": 600 },
  { "label": "960x720", "width": 960, "height": 720 },
  { "label": "1024x768", "width": 1024, "height": 768 },
  { "label": "1152x864", "width": 1152, "height": 864 },
  { "label": "1280x960", "width": 1280, "height": 960 },
  { "label": "1400x1050", "width": 1400, "height": 1050 },
  { "label": "1440x1080", "width": 1440, "height": 1080 },
  { "label": "1600x1200", "width": 1600, "height": 1200 },
  { "label": "1856x1392", "width": 1856, "height": 1392 },
  { "label": "1920x1440", "width": 1920, "height": 1440 },
  { "label": "2048x1536", "width": 2048, "height": 1536 },
  { "label": "2560x1920", "width": 2560, "height": 1920 },
  { "label": "2880x2160", "width": 2880, "height": 2160 },
  { "label": "3200x2400", "width": 3200, "height": 2400 }]

# List of common refresh rates
refresh_rates = [
    "60",
    "120",
    "144",
    "165",
    "240",
    "360"
]

# Create a temp directory in C:\Users\user\AppData\Local\
TEMP_DIR = tempfile.mkdtemp()

# Create empty batch file in C:\Users\user\AppData\Local\tmpabc123
# Temp folder name will be randomised.
open(os.path.join(TEMP_DIR, "batch_revert.bat"), "x")

# Helper function to find the relative path of nircmd.exe for .exe compilation
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Variable storing nircmd location relative for .exe compilation
nircmd = resource_path("nircmd.exe")

# On startup, get monitor current resolution. For use in reverting back to default res
for m in get_monitors():
    if m.is_primary:
        initial_res = m
        with open(os.path.join(TEMP_DIR, "batch_revert.bat"), "w") as f:
            f.write(f"@echo off\n \"{nircmd}\" setdisplay {initial_res.width} {initial_res.height} 32 240")

# Unused function for now, may be used to show what resolution you'll switch to.
def on_resolution_change(event):
    pass

# When you click the button "Launch CS2"
def on_launch_cs2():
    # Get the current resolution & refresh index
    resolution_index = combo.current()
    refresh_index = combo2.current()

    # Find the launching batch file path in temp storage
    batch_text = os.path.join(TEMP_DIR, "batch_text.bat")

    # Select resolution & refresh from list using index of selection
    selected_obj = resolutions[resolution_index]
    selected_refresh = refresh_rates[refresh_index]

    # Debug console
    print(f"Launching cs2 @", selected_obj['label'])

    # Write bat script using nircmd.exe to manipulate windows resolution.
    # Launch CS2 with launch options: -windowed -noborder -w {selected_obj['width']} -h {selected_obj["height"]} -freq {selected_refresh}
    with open(batch_text, "w") as f:
        f.write(f"@echo off\n echo {selected_obj['width']} x {selected_obj['height']} @ {selected_refresh} \n \"{nircmd}\" setdisplay {selected_obj['width']} {selected_obj['height']} 32 {selected_refresh}\n timeout /t 2 /nobreak >nul \n echo Launching CS2 \n start steam://rungameid/730//-windowed -noborder -w {selected_obj['width']} -h {selected_obj["height"]} -freq {selected_refresh}")
    subprocess.Popen(batch_text, shell=True)

    # Similar to previous function.
def on_revert_resolution():
    # Debug
    print("Attempting to revert resolution")

    # Reference location for .bat file that will handle reverting resolution
    batch_revert = os.path.join(TEMP_DIR, "batch_revert.bat")

    # Use selected refresh rate from before.
    selected_refresh = refresh_rates[combo2.current()]

    # Write nircmd bat script that reverts to default reso & refresh
    with open(batch_revert, "w") as f:
        f.write(f"@echo off\n \"{nircmd}\" setdisplay {initial_res.width} {initial_res.height} 32 {selected_refresh}")
    subprocess.Popen(batch_revert, shell=True)

# Root window options
root = tk.Tk()
root.title("CS2 AMD Resolution Util")
root.geometry("300x400")
root.iconbitmap(resource_path("headshot.ico"))

# Create UI
labels = [res["label"] for res in resolutions]

lbl = tk.Label(root, text="Select Resolution",  font = ("Times New Roman", 10))
lbl.pack(pady=20)

# Create first drop down (I know, my naming convention sucks, sue me)
combo = ttk.Combobox(root, values=labels, state="readonly")
combo.bind("<<ComboboxSelected>>", on_resolution_change)
combo.pack(pady=20, padx=20)

lbl2 = tk.Label(root, text="Select Refresh Rate", font = ("Times New Roman", 10))
lbl2.pack(pady=20)

# Create second drop down
combo2 = ttk.Combobox(root, values=refresh_rates, state="readonly")
combo2.bind("<<ComboboxSelected>>", on_resolution_change)
combo2.pack(pady=20)

# Create launch CS2 button
go_button = ttk.Button(root, text="Launch CS2", command = on_launch_cs2)
go_button.pack(pady=20)

# Create revert resolution button
revert_button = ttk.Button(root, text="Revert Resolution", command = on_revert_resolution)
revert_button.pack(pady=20 )

# Set default selection to index
combo.current(0)
combo2.current(3)

# Start app
root.mainloop()