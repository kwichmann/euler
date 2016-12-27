paths_cache = []
for i in range(0, 21):
    paths_cache.append([0] * 21)

def paths(x, y):
    if x == 0 or y == 0:
        return 1
    if paths_cache[x][y] != 0:
        return paths_cache[x][y]
    p = paths(x - 1, y) + paths(x, y - 1)
    paths_cache[x][y] = p
    return p

print(paths(20, 20))
