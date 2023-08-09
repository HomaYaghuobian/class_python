a = input('Enter your sentence :')
# اگر بخوایم حروف رو هم معکوس کنیم از کد زیر که کامنت شده استفاده میشه
# print(a[::-1])
a = a.split()
a.reverse()
a = '*'.join(a)
print(a)
