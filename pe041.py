import itertools as it
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primes = []
    
for n in range(9, 1, -1):
    if n <= 2:
        last_digits = [1]
    if n <= 6:
        last_digits = [1, 3]
    if n <= 8:
        last_digits = [1, 3, 7]
    if n == 9:
        last_digits = [1, 3, 7, 9]
    
    digits = list(range(1, n + 1))
    for num_list in list(it.permutations(digits)):
        if num_list[0] in last_digits:
            number = 0
            for i in range(0, len(digits)):
                number += num_list[i] * 10 ** i
            if is_prime(number):
                primes.append(number)
                
print(max(primes))