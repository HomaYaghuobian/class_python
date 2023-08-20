# شهریار ـ امیرمهدی ـ هما
# سینا ـ محمد ـ پوریا
# نوید ـ صدرا
# تا یکشنبه نمرات رو بکشین بالا بعد میانگین میخوره هر کی بیشتر بونس

# Function تابع
# عملیات های تکراری رو بریز تو چیزی
# که جاهای مختلف استفاده شده
# یک عملیات . یک برنامه کوچیک مثل جمع کرد دو عدد بعد هر جا که نیاز باشه صداش میزنیم
# فرقش با حلقه اینکه حلقه مثلا ۲۰ بار پشت سر همه ، تابع هر وقت که نیاز داشته باشمه
# تابع کد ما رو کوتاه تر میکنه
# def function_name():

# def s_two_number():
#     a = float(input('a: '))
#     b = float(input('b: '))

#     answer = a + b
#     print('answer:',answer)

# s_two_number()

# تابع من میتونه ورودی بگیره و حتی خروجی

def s_two_number(a,b):

    answer = a + b
    print('answer:',answer)
a = float(input('a: '))
b = float(input('b: '))

s_two_number(a,b)

# اسامی بیرون تابع با داخل داخل میتونی یکی باشه
# خروجی به معنای اینکه از داخل اتاق چیزی هم میاد بیرون

def s_two_number(a,b):

    answer = a + b
    # print('answer:',answer)
    return answer #یکی از دستور های کلیدی برای توابع
goli = float(input('a: '))
tagi = float(input('b: '))

javab = s_two_number(goli,tagi)
print(javab)

#  face detection جالبه


