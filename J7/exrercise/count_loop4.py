x = list(input('enter your sentence: '))
s = input('enter your string: ')
c = 0
for i in range(len(x)):
    if s == x[0]:
        c += 1
    x.pop(0)
print(c)