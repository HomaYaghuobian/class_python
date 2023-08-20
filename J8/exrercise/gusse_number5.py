import random
answer = int(input('answer(0,100): '))

c = 0
a = random.randint(0,100)

while True:
    print(a)
    print('"boroo bala"','"bia payin"','"Hamiine!"')
    baze = input('chetore? ')
    
    if baze == 'boroo bala':
        a = random.randint(a+1,100)
        c += 1
        continue

    elif baze == 'bia payin':
        a = random.randint(0,a)
        c += 1
        continue

    elif baze == 'Hamiine!':
        print('YoHoo')
        c += 1
        print(c)
        break