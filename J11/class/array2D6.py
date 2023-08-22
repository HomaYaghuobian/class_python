myinfo = ['homa','yaghoubian',163,['fesenjoon'],['atefeh','asma','kosar']]
print(myinfo[-1][1]) #2D
print(myinfo[-1][1][2]) #3D
# ماتریس ها در کامیوتر ها . همون ماتریکس عه

mylist = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(mylist)

for i in range(3):
    print(mylist[i])

for i in range(3):
    for j in range(3):
        print(mylist[i][j],'', end='')
    print()