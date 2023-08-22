# factorial recursive
def fact(n):
    if n == 0 :
        return 1
    else :
        return n * fact(n - 1)
n = int(input('n: '))
print(fact(n))

# fibonanchi recursive
def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
n = int(input('n: '))
print(fib(n))

# GCD recursive
def maghsom(a):
    list_a = []
    for i in range(2,a+1):
        if a % i == 0 :
            list_a.append(i)
    return list_a

def GCD(a,b):
    list_a = maghsom(a)
    list_b = maghsom(b)
    for num in list_a:
        for number in list_b:
            if num == number:
                print('GCD: ',num)
                return num
            