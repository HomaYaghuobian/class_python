n = int(input("n: "))

for i in range(n):
    print((n - i) * ' ', end='')
    print((i * 2 - 1) * '*')

for j in range(n, 0, -1):
    print((n - j) * ' ', end='')
    print((j * 2 - 1) * '*')