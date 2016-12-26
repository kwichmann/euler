ss = 0
sum = 0

for i in range(1, 101):
    ss += i ** 2
    sum += i

print(sum ** 2 - ss)
