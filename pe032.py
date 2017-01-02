def pandigital(num_list):
    digits = list(range(1, 10))
    for num in num_list:
        n = num
        while n > 0:
            digit = n % 10
            if not (digit in digits):
                return False
            digits.remove(digit)
            n = n // 10
    if digits == []:
        return True
    return False

products = []

for c in range(1234, 9877):
    for a in range(1, 9877):
        if c % a == 0:
            if pandigital([a, c // a, c]):
                products.append(c)
                
products = set(products)

print(sum(products))
