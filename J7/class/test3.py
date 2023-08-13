fruits = ['apple','benana','coconut']
for fruit in fruits :
    print(fruit)
    new_fruit = []
for fruit in fruits:
    fruit = fruit[::-1] + fruit[-1].upper()
    # خط بالا مشکلی داره
    new_fruit.append(fruit)
print(new_fruit)