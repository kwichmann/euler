def fac(n):
    if n == 1:
        return 1
    return n * fac(n - 1)

d = fac(100)

s = 0

while d > 0:
    s += d % 10
    d = d // 10

print(s)
