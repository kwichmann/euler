import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def rotate(n):
    n_string = str(n)
    new_string = n_string[-1] + n_string[0:len(n_string) - 1]
    return int(new_string)

def circular_prime(n):
    rot = n
    for i in range(len(str(n))):
        rot = rotate(rot)
        if not is_prime(rot):
            return False
    return True

s = 0

for i in range(1000001):
    if is_prime(i):
        if circular_prime(i):
            s += 1
            
print(s)
    
