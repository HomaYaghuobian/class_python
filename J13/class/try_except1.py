#  try
try : 
    x = 10 / 0
    print(x)
except:
    print('ye khatayi vojod dare!')

# اینو امتحان کن اگه نشد برو بعدی وگرنه بعدی رو حتی نگاه نمیکنه
# در صورتی که خطا ها رو نبینه
finally:
    pass
else:
    
# هندل کردن خطا ها 
# توی ماشسن حساب از اینکه تو تقسیم صفر بزاره
# خطا رو بفهم و از این استفاده کردن رو رعایت کن
try : 
    x = 10 / 0
    print(x)
except Exception as e:  # e is name.. e -> error
    print(e)

try:
    print(x)
except IndexError:
    print('khate 4')
except NameError:
    print('Khat 6')