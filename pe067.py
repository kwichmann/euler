with open ("data/pe067.txt", "r") as myfile:
    f = myfile.readlines()

t = []

for lin in f:
    t.append(list(map(int, lin.split(" "))))

def next_max(prev_max, new_line):
    next = []
    for i in range(0, len(new_line)):
        n_max = new_line[i]
        left_max = prev_max[max(0, i - 1)]
        right_max = prev_max[min(len(prev_max) - 1, i)]
        n_max += max(left_max, right_max)
        next.append(n_max)
    return next

m_list = t[0]

for i in range(1, len(t)):
    m_list = next_max(m_list, t[i])

print(max(m_list))
        

