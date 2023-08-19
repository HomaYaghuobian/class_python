a = input('enter your sentence: ')

numbers = [0]
for letter in a:
    if (letter == '0'):
        letter = int(letter)
        numbers.append(letter)
        continue
    elif (letter == '1'):
        letter = int(letter)
        numbers.append(letter)
        continue
    elif (letter == '2'):
        letter = int(letter)
        numbers.append(letter)
        continue
    elif (letter == '3'):
        letter = int(letter)
        numbers.append(letter)
        continue
    elif (letter == '4'):
        letter = int(letter)
        numbers.append(letter)
        continue
    elif (letter == '5'):
        letter = int(letter)
        numbers.append(letter)
        continue
    elif (letter == '6'):
        letter = int(letter)
        numbers.append(letter)
        continue
    elif (letter == '7'):
        letter = int(letter)
        numbers.append(letter)
        continue
    elif (letter == '8'):
        letter = int(letter)
        numbers.append(letter)
        continue
    elif (letter == '9'):
        letter = int(letter)
        numbers.append(letter)
        continue
    else:
        continue

c = 0 
for number in numbers: 
    c = number + c 

print(c)



# یک فور نوع دو و بعدش حلقه نوع اخر و یک متدی که نشون میداد اعداده یا نه بعد اینت میکنیم و اخر سر جمعش میکنیم
