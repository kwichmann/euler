def is_palin(ns):
    if len(ns) == 0 or len(ns) == 1:
        return True
    if ns[0] == ns[len(ns) - 1]:
        return is_palin(ns[1:len(ns) - 1])
    return False

def dec_to_bin(n):
    if n < 2:
        return str(n)
    return dec_to_bin(n // 2) + str(n % 2)
    
s = 0

for i in range(1, 1000001):
    if is_palin(str(i)):
        if is_palin(dec_to_bin(i)):
            s += i

print(s)
