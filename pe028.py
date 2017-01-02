diag = 1

for n in range(1, 501):
    diag += 4 * (2 * n + 1) ** 2 - 2 * n - 4 * n - 6 * n

print(diag)
