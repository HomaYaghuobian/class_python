a = int(input('a: '))
#a = 'yes' if a / 7 == 0 else a + 1
if a % 7 == 0 :
    print('yes')
else:
    a += 1 
    if a % 7 == 0 :
        print('no but',a,'yes')
    else:
        a += 1
        if a % 7 ==0 :
            print('no but',a,'yes')
        else:
            a += 1
            if a % 7 ==0 :
                print('no but',a,'yes')
            else:
                a += 1 
                if a % 7 ==0 :
                    print('no but',a,'yes')
                else:
                    a += 1 
                    if a % 7 ==0 :
                        print('no but',a,'yes')
                    else:
                        a += 1
                        if a % 7 ==0 :
                            print('no but',a,'yes')