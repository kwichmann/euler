def pyth(a, b, c):
    return a ** 2 + b ** 2 == c ** 2

def num_sol(p):
    num = 0
    for a in range(1, p):
        for b in range(a, p - a):
            if pyth(a, b, p - a - b):
                num += 1
    return num

sol_max = 0
p_max = 0

for p in range(1, 1001):
    ns = num_sol(p)
    if ns > sol_max:
        sol_max = ns
        p_max = p
    
print(p_max)

            

