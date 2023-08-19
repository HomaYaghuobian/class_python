a = int(input('a: '))
b = int(input('b: '))

prime = []
if b > a:
    for i in range(a+1,b):
        c = 1
        r = 0
        while (i != 1) or (i != 0):
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

elif a > b:
    for i in range(b+1,a):
        c = 1
        r = 0
        while (i != 1) or (i != 0):
            if i % c == 0 :
                r += 1
            if c <= i:
                c += 1
                continue
            elif c > i:
                break
        if r > 2 :
            continue
        if r < 2:
            continue
        elif r == 2:
            prime.append(i)
            continue

else:
    print('None')

if len(prime) != 0:
    print(prime)