def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

fac10 = list(map(factorial, range(10)))

def fac_prod(n):
    if n < 10:
        return fac10[n]
    return fac10[n % 10] + fac_prod(n // 10)

s = 0

for n in range(10, 2000000):
    if fac_prod(n) == n:
        s += n

print(s)
