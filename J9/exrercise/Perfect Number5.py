num = int(input('num: '))
m = 0 
for i in range(1,num):
    if num % i == 0:
        m += i

if m == num:
    print('This is a whole number')
else:
    print('This is not a whole number')