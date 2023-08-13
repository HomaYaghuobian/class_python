c = 0 
while c < 3  :
    a = int(input('enter your password: '))
    s = str(a)
    if len(s) == 4:
        if a == 1358:
            print('welcome')
            break
        
        elif a == 8531:
            print('calling the polic!!')
            break

        else:
            c += 1
    else:
        print('please try again')