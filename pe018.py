with open ("data/pe018.txt", "r") as myfile:
    f = myfile.readlines()

t = []

for lin in f:
    t.append(list(map(int, lin.split(" "))))

max = 0

for i in range(0, 2 ** (len(t) - 1)):
    b = i
    s = t[0][0]
    pos = 0
    for j in range(1, len(t)):
        if b % 2 == 1:
            pos += 1
        s += t[j][pos]
        b = b // 2
    if s > max:
        max = s

print(max)
        

