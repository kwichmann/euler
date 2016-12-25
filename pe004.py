def is_palin(ns):
    if len(ns) == 0 or len(ns) == 1:
        return True
    if ns[0] == ns[len(ns) - 1]:
        return is_palin(ns[1:len(ns) - 1])
    return False

max = 0

for i in range(1, 999):
    for j in range(1, i):
        prod = i * j
        if prod > max:
            if is_palin(str(prod)):
                max = prod

print(max)
