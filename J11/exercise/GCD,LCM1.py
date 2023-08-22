# Greatest Common Divisor
def maghsom(a):
    list_a = []
    for i in range(2,a+1):
        if a % i == 0 :
            list_a.append(i)
    return list_a

def GCD(a,b):
    list_a = maghsom(a)
    list_b = maghsom(b)
    for num in list_a:
        for number in list_b:
            if num == number:
                print('GCD: ',num)
                return num

GCD(4,6)

# Least Common Multiple
def mazarab(num,num2):
    list_num = []
    max_num = num * num2
    for i in range(1 , max_num+1):
        znum = i * num
        list_num.append(znum)
    return list_num

def LCM(num,num2):
    list_num = mazarab(num , num2)
    list_num2 = mazarab(num2 , num)
    list_lcm = []
    for num in list_num:
        for number in list_num2:
            if num == number:
                list_lcm.append(num)
    lcm = list_lcm[0]
    print('LCM: ',lcm)
    return lcm

LCM(4,6)