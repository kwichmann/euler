prime20 = [2, 3, 5, 7, 11, 13, 17, 19]

def factors(n):
    f = []
    num = n
    
    while num > 1:
        for p in prime20:
            if num % p == 0:
                f.append(p)
                num /= p
                break
    return f

def pick_factors(new_factors, old_factors):
    n = new_factors[:]
    n2 = n[:]
    o = old_factors[:]
    for f in n2:
        if f in o:
            del n[n.index(f)]
            del o[o.index(f)]
    return n

num_f = []

for i in range(1, 21):
    i_fac = factors(i)
    print("Factors of " + str(i) + ":", i_fac)

    pick = pick_factors(i_fac, num_f)
    num_f += pick
    
    print("New factors", pick, "Total factors", num_f)
    
prod = 1

for f in num_f:
    prod *= f

print(prod)
