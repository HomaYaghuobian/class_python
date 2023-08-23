a = 9 
# if a > 5:
#     ans = 'Biger'
# else:
#     ans = 'NO Biger'
ans = 'Biger' if a > 5 else 'No' # درستش کن 

mylist = []
for i in range(10):
    mylist.append(i)
print(mylist)
# or

mylist = [x for x in range(10)]
print(mylist)

mylist = [(x != 9) for x in range(10)]
print(mylist)

mylist = [x for x in range(10) if x != 9]
print(mylist)

# short hand if + short hadn list
fruits = ['mango','watermelon','banana','orange']
fruits_without_e = [fruits for fruits in fruits if 'e' not in fruits]
print(fruits_without_e)




# پایان پایتون مقدماتی***************