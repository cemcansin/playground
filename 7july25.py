import time
import random

cube = ["#", "#", "#", "#"]

for i in range(10):  # Run 10 times as an example
    print("Cube state:", cube)

    # Change each element randomly
    for j in range(len(cube)):
        cube[j] = random.choice(["#", " "])  # Flicker between "#" and space

    time.sleep(0.3)  # Pause so you can see the change
