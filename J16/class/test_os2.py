import os  # ادرس ها

ans = os.getcwd()  #ادرسی که سیستم در حال حاضر هست رو میده 
print()
print(ans)
print()
print(ans.split('//')[-1])

os.chdir() #
os.mkdir('J17') # میسازه
# اگه مجدد بزنی خطا میده
os.makedirs #بالایی با بازگشتی پوشه های قبلی که ندارم رو میسازه
s= os.path.join(os.getcwd() + '\\test.py') # ادرس های مختلف رو میده ادرس کامل تر میشه ادرس کامل تر 

l = os.listdir() # تمام اون فایل ها رو بیان میکنه
print(l)
os.remove() # پاک میکنه
os.rename() # اسم فایل رو عوض میگنه

print()

os.systemcls #پاک کردنه؟
