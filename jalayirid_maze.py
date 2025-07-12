import random
import csv

# settings
GRID_WITH = 20
GRID_HEIGHT = 18
NUM_ROOMS = 5

def create_room(min_size=3, max_size=6):
    w = random.randint(min_size, max_size)
    h = random.randint(min_size, max_size)
    x = random.randint(1, GRID_WITH - w - 1)
    y = random.randint(1, GRID_HEIGHT - h - 1)
    return (x, y, w, h)

def generate_dungeon():
    # 1 = wall  0 = floor
    grid = [[1 for _ in range(GRID_WITH)] for _ in range(GRID_HEIGHT)]
    rooms = []

    #generate rooms
    for _ in range(NUM_ROOMS):
        x, y, w, h = create_room()
        rooms.append((x, y, w, h))
        #carve out room
        for i in range(y, y + h):
            for j in range(x, x + w):
                grid[i][j] = 0
    #corridors
    for i in range(len(rooms) - 1):
        x1, y1, w1, h1 = rooms[i]
        x2, y2, w2, h2 = rooms[i + 1]
        #connect center of room
        cx1, cy1 = x1 + w1 // 2, y1 + h1 // 2
        cx2, cy2 = x2 + w2 // 2, y2 + h2 // 2
        #horizontal
        for j in range(min(cx1, cx2), max(cx1, cx2) + 1):
            grid[cy1][j] = 0
        #vertical
        for i in range(min(cy1, cy2), max(cy1, cy2) + 1):
            grid[i][cx2] = 0
    return grid

#export csv
dungeon = generate_dungeon()
with open('dungeon.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(dungeon)
print("Dungeon generated as 'dungeon.csv' ! ")


