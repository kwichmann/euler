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

prime_list = [2]

for i in range(1, 10002):
    n = next_prime(prime_list)
    prime_list.append(n)

print(n)
