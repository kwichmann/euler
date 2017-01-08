import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    
def shift_left(n):
    s = str(n)
    return int(s[1:len(s)])

def shift_right(n):
    s = str(n)
    return int(s[0:len(s) - 1])
    
def trunc_prime(n):
    if not is_prime(n):
        return False
    
    l_n = n
    while l_n >= 10:
        l_n = shift_left(l_n)
        if not is_prime(l_n):
            return False
    
    r_n = n
    while r_n >= 10:
        r_n = shift_right(r_n)
        if not is_prime(r_n):
            return False
    
    return True
    
trunc_count = 0
n = 11
s = 0

while trunc_count < 11:
    if trunc_prime(n):
        s += n
        trunc_count += 1
    n += 2

print(s)