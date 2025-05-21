import subprocess
import time
import tkinter as tk
from PIL import Image, ImageTk

# Configuration
ip_address = "8.8.8.8"
success_image_path = "success.jpg"
failure_image_path = "failure.jpg"
interval = 10  # seconds between checks

# Initialize tkinter window
window = tk.Tk()
window.attributes('-fullscreen', True)  # Make the window full screen
window.configure(background='black')

# Allow exiting fullscreen with Esc key
def exit_fullscreen(event):
    window.attributes('-fullscreen', False)
window.bind("<Escape>", exit_fullscreen)

# Get screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Image display label
label = tk.Label(window, bg='black')
label.pack(expand=True, fill='both')

# Load and show image
def update_image(image_path):
    try:
        img = Image.open(image_path)
        img = img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        tk_img = ImageTk.PhotoImage(img)
        label.config(image=tk_img)
        label.image = tk_img
    except Exception as e:
        print(f"Failed to open the image '{image_path}': {e}")

# Ping the IP
def ping_ip(ip, count=5):
    try:
        result = subprocess.run(
            ["ping", "-c", str(count), ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout.count("bytes from")
    except Exception as e:
        print(f"Ping error: {e}")
        return 0

# Main loop function
def monitor():
    success_count = ping_ip(ip_address, 5)
    
    if success_count == 5:
        print("All pings successful.")
        update_image(success_image_path)
    elif success_count == 0:
        print("All pings failed.")
        update_image(failure_image_path)
    else:
        print(f"Partial success: {success_count}/5 pings. No image change.")

    window.after(interval * 1000, monitor)

# Start monitoring
monitor()
window.mainloop()
