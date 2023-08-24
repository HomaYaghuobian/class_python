# Exception 

# ZeroDivisionError	خطای خاص از تقسیم عدد بر صفر
x = 10 / 0
print(x)
# TypeError	ورودی تابع از نوع شئ قابل‌قبول نیست

# ValueError	مقدار آرگومان ورودی تابع اشتباه است
num = "25sabz68"
print( int(num) ) 

# NameError
print(y)

# SyntaxError

# IndexErro هنگامی به وقوع می‌پیوندد اندیس یک توالی خارج از طیف باشد.

# KeyError هنگامی به وقوع می‌پیوندد که یک کلید در دیکشنری یافت نشود.

# RuntimeError	هنگامی به وقوع می‌پیوندد که خطا در هیچ یک از دسته‌های دیگر قرار نگیرد.
# این اخری باحاله 



#  finally
# برای اطمینان از اینکه کد اجرا می شود مهم نیست چه خطایی رخ می دهد،
#  شما می توانید یک بیانیه finally را استفاده کنید
#  بیانیه finally در پایین یک بیانیه try/except قرار می گیرد.
# کد شامل finally همیشه بعد از اجرای کد در try و احتمالا در بلاک except ها اجرا می شود.
# کد finally حتی زمانی که یکی از Exception ها عمل نکند هم به کار خود ادامه خواهد داد.
try:
   print("Hello")
   print(1 / 0)
except ZeroDivisionError:
   print("Divided by zero")
finally:
   print("This code will run no matter what")

# else
if  1 + 1 == 2 : #conditions
   pass
    # statement 1
else: # در غیر این صورت
    # statement 2
    pass