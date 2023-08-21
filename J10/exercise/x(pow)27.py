# y = ax**2 + bx + c
import math
def x2(a,b,c):
    pow = math.pow(b,2)
    ans = pow - (4*(a*c))

    if ans > 0:
        delta = math.sqrt(ans)
        answer = (-b + delta) / (2*a)
        answer1 = (-b - delta) / (2*a)
        answer = answer , answer1
        return answer
        
    
    elif ans == 0:
        answer = -b / 2*a
        return answer
    
    elif ans < 0:
        answer = 'It has no real roots'
        return answer

print(x2(1,5,4))
