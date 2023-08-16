# add - remove - discard - update 
colors = {'blue','yellow','black','gray','yellow'}
print(colors)

colors.add('white')
print(colors)

colors.remove('yellow')  # به این دلیل هنوز یک زرد در محموعه میبینید که من دو زرد در مجموعه زده بودم
print(colors)

colors.discard('blue')
print(colors)
# فرقش با متد remove
# اینکه در اون متد اگه اون آیتم وجود نداشته باشه خطا میده
names = {'ali','alireza','hoseyn'}
colors.update(names)
print(colors)

# count - index
num = (1,2,3,4,5,3,26,75,4,1,6,8,-1)
print(num)

x = num.count(5)
y = num.count(3)
print(x,y)

x = num.index(5)
y = num.index(3)
print(x,y)

# copy - clear - pop - update - get
mydict = {"Homa" : "17", "Alireza" : "11" , "Hoseyn" : "17.5"}
print(mydict)

x = mydict.copy()
print(x)

y = mydict.pop("Hoseyn")  # or mydict.pop('Hoseyn')
print(y)

mydict.update({"Amin":"19"})
print(mydict)

a = mydict.get("Alireza")
b = mydict.get("mohammad",16)
print(a,b)

mydict.clear()
print(mydict)