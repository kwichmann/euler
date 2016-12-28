ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def num_to_text(n):
    if n < 20:
        return ones[n]
    if n < 100:
        return tens[(n // 10) - 2] + ones[n % 10]
    if n < 1000:
        txt = ones[n // 100] + "hundred"
        if n % 100 != 0:
            txt += "and" + num_to_text(n % 100)
        return txt
    return "onethousand"

sum = 0

for i in range(1, 1001):
    sum += len(num_to_text(i))

print(sum)

    
