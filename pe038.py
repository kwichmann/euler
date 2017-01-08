import math

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

def multiple(num, n):
    l = []
    for i in range(1, n + 1):
        l.append(i * num)
    return l
    
def pan_number(mult):
    s = ""
    for i in range(0, len(mult)):
        s += str(mult[i])
    return int(s)

pan_max = 0

for n in range(2, 10):
    for num in range(10 ** (math.floor(9 / n) - 1), 10 ** math.floor(9 / n)):
        mult = multiple(num, n)
        if pandigital(mult):
            pn = pan_number(mult)
            if pn > pan_max:
                pan_max = pn

print(pan_max)

            

