import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def quadratic_primes(a, b):
    n = 0
    while is_prime(n ** 2 + a * n + b):
        n += 1
    return n

max_n = 0
max_a = 0
max_b = 0

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        qp = quadratic_primes(a, b)
        if qp > max_n:
            max_n = qp
            max_a = a
            max_b = b

print(max_a, max_b, max_a * max_b)
