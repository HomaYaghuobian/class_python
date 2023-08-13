numbers = [10 , 11, 0,18,17,11,77,3,5, -9]
print(numbers)
finel_number = []
for number in numbers:
    number_plus_2 = number + 2
    finel_number.append(number_plus_2)
print(finel_number)

numbers = [10 , 11, 0,18,17,11,77,3,5, -9]
finel_number = []
for i in range(len(numbers)):
    number_plus = numbers[i] + i
    finel_number.append(number_plus)
print(finel_number)