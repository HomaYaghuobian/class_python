username_a = 'aa'
password_a = 123
username_b = 'bb'
password_b = 321
username_c = 'cc'
password_c = 231
username = input('username: ')
password = int(input('password: '))
if username == username_a:
    if password == password_a:
        print('welcom')
    else:
        password = int(input('password: '))
        if password == password_a:
            print('welcom')
        else:
            print('you are not registered')
elif username == username_b:
    if password == password_b:
        print('welcom')
    else:
        password = int(input('password: '))
    if password == password_b:
        print('welcom')
    else:
        print('you are not registered')
elif username == username_c:
    if password == password_c:
        print('welcom')
    else:
        password = int(input('password: '))
    if password == password_c:
        print('welcom')
    else:
        print('you are not registered')
else :
    print('you are not registered')