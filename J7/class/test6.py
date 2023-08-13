# mylist = list(input())
# [1 ,2 ,3]
# print(mylist)
# 1 2 3
# 123
s_l = input('adad ra ba yek fasele(apace) vared konid: ')
l = s_l.split()
for i in range(len(l)):
    l[i] = int(l[i])
print(l)