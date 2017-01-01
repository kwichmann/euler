def fac_sum(n):
    f = []
    for i in range(1, n):
        if n % i == 0:
            f.append(i)
    return sum(f)

abundant = []

for i in range(1, 28124):
    if fac_sum(i) > i:
        abundant.append(i)

s = list(range(28124))

for i in abundant:
    for j in abundant:
        if i + j < 28124:
            s[i + j] = 0
        else:
            break

print(sum(s))
