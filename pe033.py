def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def reduce(f):
    n = f[0]
    d = f[1]
    g = gcd(n, d)
    return [n // g, d // g]

numerators = []
denominators = []

for n10 in range(1, 10):
    for n1 in range(1, 10):
        for d1 in range(1, 10):
            d10 = n1
            n = 10 * n10 + n1
            d = 10 * d10 + d1
            if d > n:
                if reduce([n, d]) == reduce([n10, d1]):
                    numerators.append(n)
                    denominators.append(d)

for n10 in range(1, 10):
    for n1 in range(1, 10):
        for d1 in range(1, 10):
            n10 = d1
            n = 10 * n10 + n1
            d = 10 * d10 + d1
            if d > n:
                if reduce([n, d]) == reduce([n1, d10]):
                    numerators.append(n)
                    denominators.append(d)

n_prod = 1
d_prod = 1

for n in numerators:
    n_prod *= n

for d in denominators:
    d_prod *= d

print(reduce([n_prod, d_prod]))
