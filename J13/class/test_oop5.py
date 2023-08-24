# برنامه نویسی مربوط با اشیا
# Object Oriented Progeraming

# نشون دهنده ست مثلا کلاس انسان .. میگن کلاس فلان
# شی یک چیزیه ک از یک کلاس میسازن

# فقط حرف اول بزرگ باقی کوچک اسامی کلاس رو کپتالایز بنویس
class Person:
    # properties ویژگی ها مثلا شنواست یا نه
    name = None #نمیتونم اسمش رو بزاری پوریا چون همه آدما که پوریا نیستن
    lastname = None
    nationality = 'Iran'
    # مثال
    heir_color = None
    nationality_id = None

    # Mothids توابع داخل کلاس مثلا راه رفتن برای انسان
    def eat():
        pass

    def sleep():
        pass

    def working():
        pass

    def walking():
        pass
    # int , str , ... کلاسن
    # type(1) --> class int

    pass

p1 = Person() #شی پی ۱ را از کلاس پرسن ساختم
p2 = Person()
p3 = Person()
# با مفاهیم کد میزنیم
n = input('enter your nationality: ')
p1.nationality = n
print(p1.nationality)
print(p2.nationality)
print(type(p1))
# new class
