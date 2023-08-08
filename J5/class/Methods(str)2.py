a = 'amir mahdi'
# upper _ Lower
# isupper _ islower
print(a.islower())
print(a.upper())
print(a[-1].islower)
print(a[:4].isupper)
# coplitalize _ title
print(a.capitalize())
print(a.title())
# startswith _ endwith
print(a.startswith('A'))
print(a.endswith('i'))
# count
print(a.lower().count('a'))
# find
print(a.find('h'))
print(a.lower().find('i'))
b = 'amir mahdimahdi mahdi'
print(b.lower().count('mahdi'))
c = 'mamam'
print(c.count('mam'))
# replace
print(a.replace('mahdi','ALI'))
print(a.lower().replace('a','A')) 