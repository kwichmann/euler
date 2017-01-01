with open ("data/pe022.txt", "r") as myfile:
    f = myfile.read()

names = f.replace('"', "").split(",")
names = sorted(names)

s = 0

for i in range(len(names)):
    score = 0
    for j in range(len(names[i])):
        score += (ord(names[i][j]) - 64)
    s += score * (i + 1)

print(s)
