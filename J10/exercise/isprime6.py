prime = [2]
for i in range(3,98):
    c = 1
    r = 0
    while (i != 1) and (i != 0) and (i % 2 != 0):
        if i % c == 0 :
            r += 1
        if c <= i:
            c += 1
            continue
        elif c > i:
            break
    if r > 2 or r < 2:
        continue
    elif r == 2:
        prime.append(i)
print(prime)