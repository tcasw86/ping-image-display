import subprocess
from PIL import Image

# IP address to ping
ip_address = "8.8.8.8"  # Change to the desired IP address

# Image paths
success_image_path = "success.jpg"  # Image to show on success
failure_image_path = "failure.jpg"  # Image to show on failure

def ping_ip(ip, count=5):
    try:
        # Run the ping command
        result = subprocess.run(
            ["ping", "-c", str(count), ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        # Count successful responses from the ping output
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
    successful_pings = ping_ip(ip_address, 5)
    
    if successful_pings == 0:
        print("All pings failed. Showing failure image.")
        show_image(failure_image_path)

    else:
        print("All pings successful. Showing success image.")
        show_image(success_image_path)
