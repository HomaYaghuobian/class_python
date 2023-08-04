a = float(input('a: '))
if a % 10 > 6 and a % 2 == 0 and a >= 0:
    print('A')
# n[>10] =B ?!
elif a % 10 <4 and a % 2 ==0 and a >= 0:
    print('B')
elif a <= 0:
    print('D')
else :
    print('C')