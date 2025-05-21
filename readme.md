# Ping Image Display Python Script
This is a simple python script that runs a 5 ping tests, and based on the result with either show a fullscreen checkmark image or an X if failing. This was created to demonstrate simple networking to children. The demonstration being two raspberry pis pinging each other. When a cable is connected both screens would show a green checkmark, when disconnected both displays show a red X.

The was created and intended to run on Ubuntu desktop with no screen timeout and automatic log in enabled.

## Sections

### Dependencies 
The following Libraries are used:
- `Pillow` (for image handling)
- `tkinter` (standard in most Python installations)
  
### Ubuntu Packages (if missing)
sudo apt install python3-pil python3-pil.imagetk python3-tk

###  AutoStart
Option 1: Autostart After Login (GUI Session)
* Enable auto-login for your user (Ubuntu Settings > Users).
* Create a .desktop autostart entry:
mkdir -p ~/.config/autostart
nano ~/.config/autostart/network_monitor.desktop


### Modifications
Full Image paths are used, Update .py script:
SUCCESS_IMAGE = "/home/yourusername/Pictures/success.jpg"
FAILURE_IMAGE = "/home/yourusername/Pictures/failure.jpg"

Full path to Python script needed for ping-image-display.py in network_monitor.desktop:
Exec=/usr/bin/python3 /full/path/to/your_script.py
