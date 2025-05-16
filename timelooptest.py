import subprocess
from PIL import Image
import time

# IP address to ping
ip_address = "8.8.8.8"  # Change to your desired IP

# Image paths
success_image_path = "success.jpg"  # Show this on 5/5 successful pings
failure_image_path = "failure.jpg"  # Show this on 0/5 successful pings

# Ping interval (seconds)
interval = 10

def ping_ip(ip, count=5):
    try:
        result = subprocess.run(
            ["ping", "-c", str(count), ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        success_count = result.stdout.count("bytes from")
        return success_count
    except Exception as e:
        print(f"Error while pinging: {e}")
        return 0

def show_image(path):
    try:
        img = Image.open(path)
        img.show()
    except Exception as e:
        print(f"Failed to open image: {e}")

if __name__ == "__main__":
    print("Starting continuous ping monitoring. Press Ctrl+C to stop.")
    while True:
        successful_pings = ping_ip(ip_address, 5)
        
        if successful_pings == 5:
            print("✅ All pings successful. Showing success image.")
            show_image(success_image_path)
        elif successful_pings == 0:
            print("❌ All pings failed. Showing failure image.")
            show_image(failure_image_path)
        else:
            print(f"⚠️ Partial success: {successful_pings}/5 pings.")

        time.sleep(interval)
