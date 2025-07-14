import random
import csv

# settings
GRID_WIDTH = 20
GRID_HEIGHT = 18
NUM_ROOMS = 9
MAX_ROOM_TRIES = 30  # max tries per room to avoid infinite loops

def create_room(min_size=3, max_size=6):
    w = random.randint(min_size, max_size)
    h = random.randint(min_size, max_size)
    x = random.randint(1, GRID_WIDTH - w - 1)
    y = random.randint(1, GRID_HEIGHT - h - 1)
    return (x, y, w, h)

def rooms_overlap(room1, room2):
    x1, y1, w1, h1 = room1
    x2, y2, w2, h2 = room2
    return (
        x1 < x2 + w2 and
        x1 + w1 > x2 and
        y1 < y2 + h2 and
        y1 + h1 > y2
    )

def generate_dungeon():
    grid = [[1 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    rooms = []

    for _ in range(NUM_ROOMS):
        for _ in range(MAX_ROOM_TRIES):
            new_room = create_room()
            if all(not rooms_overlap(new_room, other) for other in rooms):
                rooms.append(new_room)
                x, y, w, h = new_room
                for i in range(y, y + h):
                    for j in range(x, x + w):
                        grid[i][j] = 0
                break  # room successfully added, stop trying
        else:
            print("⚠️ Could not place a room after many tries!")

    # connect rooms with corridors
    for i in range(len(rooms) - 1):
        x1, y1, w1, h1 = rooms[i]
        x2, y2, w2, h2 = rooms[i + 1]
        cx1, cy1 = x1 + w1 // 2, y1 + h1 // 2
        cx2, cy2 = x2 + w2 // 2, y2 + h2 // 2

        # horizontal corridor
        for j in range(min(cx1, cx2), max(cx1, cx2) + 1):
            grid[cy1][j] = 0
        # vertical corridor
        for i in range(min(cy1, cy2), max(cy1, cy2) + 1):
            grid[i][cx2] = 0

    return grid

# export CSV
dungeon = generate_dungeon()
with open('dungeon.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(dungeon)

print("✅ Dungeon generated as 'dungeon.csv' with non-overlapping rooms!")
