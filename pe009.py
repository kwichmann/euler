def is_pyth(a, b, c):
    return (a ** 2 + b ** 2 == c ** 2)

for c in range(1, 999):
    for b in range(1, 999 - c):
        a = 1000 - b - c
        if is_pyth(a, b, c):
            print(a, b, c)
            print(a * b * c)
            break

