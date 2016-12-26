import math

def is_prime(p):
    for i in range(2, round(math.sqrt(p) + 1)):
        if p % i == 0:
            return False
    return True

sum = 2
n = 3

while n < 2000000:
    if is_prime(n):
        sum += n
    n += 2

print(sum)
