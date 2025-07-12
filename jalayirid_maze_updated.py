import random
import csv
from PIL import Image

# settings
GRID_WIDTH = 20
GRID_HEIGHT = 18
NUM_ROOMS = 5

def create_room(min_size=3, max_size=6):
    w = random.randint(min_size, max_size)
    h = random.randint(min_size, max_size)
    x = random.randint(1, GRID_WIDTH - w - 1)
    y = random.randint(1, GRID_HEIGHT - h - 1)
    return (x, y, w, h)

def generate_dungeon():
    grid = [[1 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    rooms = []

    for _ in range(NUM_ROOMS):
        x, y, w, h = create_room()
        rooms.append((x, y, w, h))
        for i in range(y, y + h):
            for j in range(x, x + w):
                grid[i][j] = 0

    for i in range(len(rooms) - 1):
        x1, y1, w1, h1 = rooms[i]
        x2, y2, w2, h2 = rooms[i + 1]
        cx1, cy1 = x1 + w1 // 2, y1 + h1 // 2
        cx2, cy2 = x2 + w2 // 2, y2 + h2 // 2

        for j in range(min(cx1, cx2), max(cx1, cx2) + 1):
            grid[cy1][j] = 0
        for i in range(min(cy1, cy2), max(cy1, cy2) + 1):
            grid[i][cx2] = 0

    return grid

# Generate dungeon
dungeon = generate_dungeon()

# Export CSV
with open('dungeon.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(dungeon)

print("Dungeon CSV generated as 'dungeon.csv'!")

# Convert to image
tile_size = 8  # GB Studio tiles are usually 8x8 pixels
img = Image.new("RGB", (GRID_WIDTH * tile_size, GRID_HEIGHT * tile_size), "white")

for y, row in enumerate(dungeon):
    for x, cell in enumerate(row):
        color = (0, 0, 0) if cell == 1 else (255, 255, 255)  # Wall = black, floor = white
        for i in range(tile_size):
            for j in range(tile_size):
                img.putpixel((x * tile_size + i, y * tile_size + j), color)

img.save("dungeon.png")
print("Dungeon image generated as 'dungeon.png'! Ready to import to GB Studio!")
