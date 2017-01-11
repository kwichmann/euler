with open ("data/pe042.txt", "r") as myfile:
    f = myfile.read()

words = f.replace('"', "").split(",")

def word_value(word):
    value = 0
    for i in range(0, len(word)):
        value += ord(word[i]) - 64
    return value

def is_triangle(num):
    n = 0
    while num >= n * (n + 1) // 2:
        if n * (n + 1) // 2 == num:
            return True
        n += 1
    return False
    
coded = 0
for word in words:
    if is_triangle(word_value(word)):
        coded += 1

print(coded)