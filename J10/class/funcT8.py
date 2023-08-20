# functions --> 1 : built in function = print() که تو خودش هست
# --> 2 : library function = shape() توابعی که توی کتابخانه ها هستن
#  --> 3: our function = خودت میخوای در بیاری مثل معادله درجه اول

# حقوق یک کارمندی رو حساب کنم
def salary_calculator(salary_TpH,h,tax): 
    base_salary = float(salary_TpH) * h
    tax = tax / 100 
    base_salary = base_salary - (base_salary * tax)
    print(base_salary)

salary_calculator('60000',160,10)


def salary_calculator(salary_TpH,h,tax=10 ): # مقدار پیش فرض دادیم و اگه ما بدیم اونی که دادیم رو در نظر میگیره و موارد پیش فرض رو باید اخر بزاریم.. و چیزایی رو پیش فرض بزاریم که معلوق باشه نه
    base_salary = float(salary_TpH) * h
    tax = tax / 100 
    base_salary = base_salary - (base_salary * tax)
    print(base_salary)

salary_calculator('60000',160)
salary_calculator('60000',160,30)