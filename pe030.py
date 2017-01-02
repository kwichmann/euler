def fifth(n):
    if n < 10:
        return n ** 5
    return (n % 10) ** 5 + fifth(n // 10)

# We just need to check for up to 9 ** 5 * 6,
# Since n = 6 is the first for which 9 ** 5 * n > 10 ** n

s = 0

for i in range(10, 9 ** 5 * 6 + 1):
    if fifth(i) == i:
        s += i

print(s)
