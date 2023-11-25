import subprocess
from colorama import Fore, Style, init
import pyfiglet

init(autoreset=True)

header_text = "Show Password Wifi"
colored_header = Fore.RED + pyfiglet.figlet_format(header_text) + Style.RESET_ALL

print(colored_header)

insta_text = (
    "--------------------------------------------------\n"
    f"|{Fore.RED}INSTAGRAM{Fore.YELLOW} ==> {Fore.CYAN}https://www.instagram.com/r94xs/{Style.RESET_ALL}   |\n"
    "--------------------------------------------------"
)
print(insta_text)

meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
data = meta_data.decode('utf-8', errors="backslashreplace")
data = data.split('\n')

profiles = []

for line in data:
    if "All User Profile" in line:
        parts = line.split(":")
        wifi_name = parts[1].strip()
        profiles.append(wifi_name)

print("{:<30}| {:<}".format("name wifi network", "password"))
print("----------------------------------------------")

for profile in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'])
        results = results.decode('utf-8', errors="backslashreplace")
        results = results.split('\n')
        password = [line.split(":")[1].strip() for line in results if "Key Content" in line]
        if password:
            print("{:<30}| {:<}".format(profile, password[0]))
        else:
            print("{:<30}| {:<}".format(profile, ""))
    except subprocess.CalledProcessError:
        print("ERROR")
