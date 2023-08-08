mylist = [1, 2, 3, 4, 5]
print(mylist)
print(len(mylist))
print(mylist[3])

fruits = ['apple','benana','pineapple']
print(fruits[1:5:2])
# len s okay
# l = [] == l = list()
print(fruits[::-1])
a= [1,2.5,True,'ali',['bmw','benz']]
print(type(a[4]))
print(type(a[4][1]))
print(a[3][-2])

l =  [1,2,3]
k = [4,5,6]
print(l +k)
print(l * 3)
# []*[] no! 
l[0] = 78
print(l)