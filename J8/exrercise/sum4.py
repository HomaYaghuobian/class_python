a = int(input('a: '))
b = int(input('b: '))
c = 0 
if a > b:
    for i in range(b+1,a):
        c += i
    print(c)

elif b > a:
    for i in range(a+1,b):
        c += i
    print(c)
        
else:
    print('0')