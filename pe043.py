import itertools as it

def value(n):
    v = 0
    for i in range(0, 10):
        v += n[i] * 10 ** (9 - i)
    return v

digits = list(range(0, 10))

s = 0
for n in list(it.permutations(digits)):
    if (n[1] * 100 + n[2] * 10 + n[3]) % 2 == 0:
        if (n[2] * 100 + n[3] * 10 + n[4]) % 3 == 0:
            if (n[3] * 100 + n[4] * 10 + n[5]) % 5 == 0:
                if (n[4] * 100 + n[5] * 10 + n[6]) % 7 == 0:
                    if (n[5] * 100 + n[6] * 10 + n[7]) % 11 == 0:
                        if (n[6] * 100 + n[7] * 10 + n[8]) % 13 == 0:
                            if (n[7] * 100 + n[8] * 10 + n[9]) % 17 == 0:
                                s += value(n)
print(s)