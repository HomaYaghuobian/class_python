print('1. Degree Celsius => Fahrenheit')
print('2. Degree Celsius => Kelvin')
print('3. Kelvin => Fahrenheit')
print('4. Kelvin => Degree Celsius')
print('5. Fahrenheit => Kelvin')
print('6. Fahrenheit => Degree Celsius')
print('7. exit')
u = input('Please enter the desired option: ')
while (u != '7') or (u != 'exit'):
    if (u == '1') or (u == 'Degree Celsius => Fahrenheit'):
        a = float(input('temperature: '))
        b= a * 9 / 5 + 32
        print(b,'Fahrenheit')
        u = input('Please enter the desired option: ')
    elif (u == '2') or (u == 'Degree Celsius => Kelvin'):
        a = float(input('temperature: '))
        b = a + 273.15
        print(b,'Kelvin')
        u = input('Please enter the desired option: ')
    elif (u == '3') or (u == 'Kelvin => Fahrenheit'):
        a = float(input('temperature: '))
        b = (a - 273.15) * 9 / 5 + 32
        print(b,'Fahrenheit')
        u = input('Please enter the desired option: ')
    elif (u == '4') or (u == 'kelvin => Degree Celsius'):
        a = float(input('temperature: '))
        b = a - 273.15
        print(b,'Degree Celsius')
        u = input('Please enter the desired option: ')
    elif (u == '5') or (u == 'Fahrenheit => Kelvin'):
        a = float(input('temperature: '))
        b = (a - 32) * 5 /9 + 273.15
        print(b,'Kelvin')
        u = input('Please enter the desired option: ')
    elif (u == '6') or (u == 'Fahrenheit => Degree Celsius'):
        a = float(input('temperature: '))
        b = ( a - 32)*5/ 9
        print(b,'Degree Celsius')
        u = input('Please enter the desired option: ')
    elif (u == '7') or (u == 'exit'):
        print('okay,by')
        break
    else:
        print('The selected option is incorrect')
        u = input('Please enter the desired option: ')