# توابع خاص
# recursive function  توبع بازگشتی
# کد فاکتوریل ساده
def fact(n):
    ans = 1
    for i in range(1, n+1):
        ans = ans * i
    return ans


# recursire نیازمند فرموله
# n * (n-1)! فرمول فاکتوریل
# 0! = 1 با این شرط
# درخت بازگشتی رو مینویسیم
# 4! --> 4 
#    --> 3! --> 3
#           --> 2! --> 2
#                  --> 1! --> 1
#                         --> 0! تا همینجا کافیه
# بعداز عمق ضرب میکنیم در هم بعد جواب  بدست میاد


# این توابع حتمااا return دارن
 
def fact(n):
    if n == 0 :
        return 1
    else :
        return n * fact(n - 1)

print(fact(3))

n = int(input('n: '))
print(fact(n))