poss = 0

for pound2 in range(2):
    for pound1 in range(3 - 2 * pound2):
        for pence50 in range(5 - 4 * pound2 - 2 * pound1):
            for pence20 in range(11 - 10 * pound2 - 5 * pound1 - 2 * pence50):
                for pence10 in range(21 - 20 * pound2 - 10 * pound1 - 5 * pence50 - 2 * pence20):
                    for pence5 in range(41 - 40 * pound2 - 20 * pound1 - 10 * pence50 - 4 * pence20 - 2 * pence10):
                        for pence2 in range(101 - 100 * pound2 - 50 * pound1 - 25 * pence50 - 10 * pence20 - 5 * pence10 - 2 * pence5):
                            for pence1 in range(201 - 200 * pound2 - 100 * pound1 - 50 * pence50 - 20 * pence20 - 10 * pence10 - 5 * pence5 - 2 * pence2):
                                if pence1 + 2 * pence2 + 5 * pence5 + 10 * pence10 + 20 * pence20 + 50 * pence50 + 100 * pound1 + 200 * pound2 == 200:
                                    poss += 1

print(poss)
