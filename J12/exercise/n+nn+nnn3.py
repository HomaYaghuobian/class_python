def number(n):
    n = str(n)
    n1 = n
    n2 = n+n
    n3 = n+n+n
    return int(n1) + int(n2)+ int(n3)

n = int(input('n: '))

answer = number(n)
print(answer)