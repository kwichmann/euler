with open ("data/pe011.txt", "r") as myfile:
    f = myfile.readlines()

grid = []
for g in f:
    l = map(int, g.replace("\n", "").split(" "))
    grid.append(list(l))

d = [[0, 1], [1, 0], [1, 1], [1, -1]]

def new_grid(start, direction, mult):
    x = start[0] + direction[0] * mult
    y = start[1] + direction[1] * mult
    return [x, y]

def in_grid(cell):
    return not(cell[0] < 0 or cell[0] > 19 or cell[1] < 0 or cell[1] > 19)

def new_value(start, direction, mult):
    n = new_grid(start, direction, mult)
    return grid[n[1]][n[0]]

def product(start, direction):
    prod = 1
    for i in range(4):
        prod *= new_value(start, direction, i)
    return prod

max = 0

for i in range(20):
    for j in range(20):
        for direction in d:
            if in_grid(new_grid([i, j], direction, 3)):
                p = product([i, j], direction)
                if p > max:
                    max = p

print(max)            
