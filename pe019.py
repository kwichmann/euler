months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def days(y, m):
    if m != 1:
        return months[m]
    if y % 4 != 0:
        return 28
    if y % 100 != 0:
        return 29
    if y % 400 != 0:
        return 28
    return 29

sun = 0
day = 0

for year in range(1900, 2001):
    for month in range(0, 12):
        if day == 6 and year >= 1901:
            sun += 1
        day = (day + days(year, month)) % 7

print(sun)
        
        

