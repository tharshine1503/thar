import os
import platform
import subprocess

def get_system_uptime():
    if platform.system() == "Windows":
        # For Windows systems
        try:
            output = subprocess.check_output("net stats workstation", shell=True, text=True)
            for line in output.splitlines():
                if "Statistics since" in line:
                    print("System Uptime (since):", line)
                    break
        except Exception as e:
            print("Unable to fetch uptime on Windows:", e)
    else:
        # For Unix/Linux/Mac systems
        try:
            with open('/proc/uptime', 'r') as f:
                uptime_seconds = float(f.readline().split()[0])
                uptime_hours = uptime_seconds // 3600
                uptime_minutes = (uptime_seconds % 3600) // 60
                print(f"System Uptime: {int(uptime_hours)} hours, {int(uptime_minutes)} minutes")
        except FileNotFoundError:
            # For MacOS or other systems without /proc/uptime
            try:
                output = subprocess.check_output("uptime", shell=True, text=True)
                print("System Uptime:", output.strip())
            except Exception as e:
                print("Unable to fetch uptime:", e)

if __name__ == "__main__":
    get_system_uptime()
