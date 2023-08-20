# ax + b = 0 
# x = -b / a
def x(a,b):
    ans = -b / a
    return ans

a = float(input('a: '))
b = float(input('b: '))

answer = x(a,b)
print(answer)