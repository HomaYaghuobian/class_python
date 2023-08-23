# شروع پایتون پیشرفته**

# map
# lamda
# filter

# def f(x , y):
#     return x + 2 * y
#  or 
# f = lambda x,y : x + 2 * y
# lamda در یک خط تابع میسازد
# short hand function

even = lambda number : ( number % 2 == 0)
numbers_list = [5 , 45 , 2 , 0 , -8 , 13 , 2]
print(list(filter(even,numbers_list)))  #اون شرط رو پیاده سازی میکنه
print(list(map(even , numbers_list)))   # ایا از اون قانون پیروی میکنهه یا نه