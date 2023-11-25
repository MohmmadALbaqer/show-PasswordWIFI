import os
import pyfiglet
import random
from termcolor import colored

colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

selected_color = random.choice(colors)

text = 'I N S T A L L'

lo = pyfiglet.figlet_format(text)
colored_lo = colored(lo, color=selected_color)

print(colored_lo)

libraries_to_install = [
    "subprocess",
    "Fore",
    "Style",
    "init",
    "pyfiglet",
]

for library in libraries_to_install:
    os.system(f"pip install {library}")
