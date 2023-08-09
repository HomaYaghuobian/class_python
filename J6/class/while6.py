a = float(input('score: '))
s = 0
c = 0
while a != -1:
    s += a
    c += 1
    a = float(input('score: '))
print(s) # sum
print(s / c)