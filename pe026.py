def reciprocal_periodicity(n):
    remainders = [1]
    while True:
        r = remainders[-1] % n
        if r == 0:
            return 0
        d = r * 10
        if d in remainders:
            return len(remainders) - remainders.index(d)
        remainders.append(d)

m_cycle = 0
m_number = 0

for i in range(1, 1001):
    rp = reciprocal_periodicity(i)
    if rp > m_cycle:
        m_cycle = rp
        m_number = i

print(m_number)
