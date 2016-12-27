collatz_cache = [0] * 1000000

def next_collatz(n):
    if n % 2 == 0:
        return int (n / 2)
    return 3 * n + 1

def collatz_length(n):
    cur = n
    l = 1
    while cur != 1:
        if cur < n:
            l += (collatz_cache[cur] - 1)
            collatz_cache[n] = l
            return l
        cur = next_collatz(cur)
        l += 1
    collatz_cache[n] = l
    return l

max_l = 0
max_n = 0

for i in range(1, 1000000):
    cl = collatz_length(i)
    if cl > max_l:
        max_l = cl
        max_n = i

print(max_n)
