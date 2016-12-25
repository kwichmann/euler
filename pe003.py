num = 600851475143

def divides(n, p):
    return n % p == 0

def divides_list(n, l):
    for p in l:
        if divides(n, p):
            return True
    return False

def next_prime(l):
    counter = max(l) + 1
    while divides_list(counter, l):
        counter += 1
    return counter

cur_prime = 2
prime_list = [2]

while num != 1:
    while divides(num, cur_prime):
        print(cur_prime)
        num /= cur_prime
        
    cur_prime = next_prime(prime_list)
    prime_list.append(cur_prime)
