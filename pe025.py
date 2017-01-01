f1 = 1
f2 = 1

n = 3

while True:
    f_new = f1 + f2
    if f_new >= 10 ** 999:
        print(n)
        break
    f1 = f2
    f2 = f_new
    n += 1
