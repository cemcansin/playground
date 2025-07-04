import time
import os
import random

def clear_screen():
    # Works on Windows and Unix
    os.system('cls' if os.name == 'nt' else 'clear')

cube_art = [
    "####",
    "####",
    "####",
    "####"
]

try:
    while True:
        clear_screen()
        # Randomly choose a brightness: light or dark
        if random.choice([True, False]):
            symbol = "#"
        else:
            symbol = " "

        # Print "cube" with chosen symbol
        for row in cube_art:
            print(row.replace("#", symbol))
        
        # Flicker speed
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nStopped.")
