def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

num = 999999
digits = list(range(10))
answer = ""

while digits != []:
    new_digit = num // factorial(len(digits) - 1)
    num = num % factorial(len(digits) - 1)
    answer += str(digits[new_digit])
    del digits[new_digit]

print(answer)
    
