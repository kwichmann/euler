def factor_count(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

def triangle(n):
    return int(n * (n + 1) / 2)

num = 1

while True:
    if num % 2 == 0:
        fac = factor_count(int(num / 2)) * factor_count(num + 1)
    else:
        fac = factor_count(int((num + 1)/ 2)) * factor_count(num)
    if fac > 500:
        print(triangle(num))
        quit()
    num += 1
