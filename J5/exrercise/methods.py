a = 'AMIR ali'
# تمام حروف را کوچک نشان میدهد
print(a.casefold())
b = 'benana'
# رشته مورد نظر را در مرکز قرار می دهد،با استفاده از کاراکتر مشخص شده(پیش فرض فضای خالی است)فضا را پر می کند
print(b.center(10))
print(b.center(10,'.'))
# اگر تمام مقادیر رشته حروف الفبا و اعداد باشند،درست را نمایش میدهد
print(a.isalnum())
print(b.isalnum())
# درست را زمانی نمایش میدهد که تنها رشته دارای حرف باشد
print(b.isalpha)
c = '1234'
# درست را زمانی نمایش میدهد که تنها رشته دارای رقم باشد
print(b.isdigit())
print(c.isdigit())