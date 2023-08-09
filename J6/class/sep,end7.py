# 1'2''3'''4''''5'''''6''''''
# n = 6 # input(truo)
n = int(input('n: '))
c = 1
# sep=''  , end=''
while c <= n :
    print(c , "'" * c ,sep='',end='')
    c += 1