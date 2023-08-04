print('1. -')
print('2. +')
print('3. *')
print('4. /')

op = input('enter operator:')

if (op == '1') or ( op == '+'):
    a = float(input('a:'))
    b= float(input('b:'))
    answer = a- b
    print('ANSWER IS', answer)

elif (op == '2') or (op == '-'):
    a = float(input('a:'))
    b= float(input('b:'))
    answer = a +b
    print('ANSWER IS', answer)

elif (op == '3')or (op == '*'):
    a =float(input('a:'))
    b= float(input('b:'))
    answer = a*b
    print('ANSWER IS', answer)

elif (op == '4') or (op == '/'):
    a= float(input('a:'))
    b= float(input('b:'))
    answer = a/b if b!=0 else 'no no'
    print(answer)
    
else:
    print('this operator false')