map_grid = [
    ["#","#","#","#","#"],
    ["#",".",".",".","#"],
    ["#",".","p",".","#"],
    ["#",".",".",".","#"],
    ["#","#","#","#","#"],

]

def map(map_grid):
    for row in map_grid:
        print(" ".join(row))
print("working")
print(map(map_grid))