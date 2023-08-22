#   جوابش رو .. توان های عدد اول به تعداد عدد دوم چاپ کنه تابعی
# امتحان
def power (a,b):
    for i in range(b):
        print(a ** i)
power(2,6)
num1 = int(input('a: '))
num2 = int(input('b: '))
power(num1 , num2)