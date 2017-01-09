def champ_digit(n):
    if n < 10:
        return n
    
    count = 10
    digits = 2
    while count <= n:
        last_count = count
        count += 9 * digits * 10 ** (digits - 1)
        digits += 1
    
    num = 10 ** (digits - 2) + (n - last_count) // (digits - 1)
    dig = (n - last_count) % (digits - 1)
    
    return int(str(num)[dig])

prod = 1

for i in range(0, 7):
    prod *= champ_digit(10 ** i)
    
print(prod)

