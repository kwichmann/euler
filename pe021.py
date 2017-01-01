def fac_sum(n):
    f = []
    for i in range(1, n):
        if n % i == 0:
            f.append(i)
    return sum(f)

s = 0

for i in range(1, 10001):
    fs = fac_sum(i)
    if fs != i:
        if fac_sum(fs) == i:
            s += i

print(s)
