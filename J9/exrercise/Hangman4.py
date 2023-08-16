import random
from colorama import Fore
from colorama import Back

provinces = ['khorasan','sistan','yazd','tehran','mazandaran','golestan','esfehan','markazi','ardebil','gilan']
colors = ['red','yellow','black','blue','white','gray','brown','green','purple','orange']
countries = ['america','canada','france','england','spina','china','india','italy','japan','germany','russia','argantina','australia','irland','thailand','egypt','turkey']
animals = ['cat','kangaroo','cow','lizard','horse','whall','panda','snake','sheep','wolf','owl']
animals2 = ['parrot','snail','lion','wolf','gorilla','ant','camel','rabbit','giraffe','chicken','crocodile']
foods = ['chocolate','apple','chicken','hamburger','fish','mangoes','cake','lemon','clonuts','watermelon']
foods2 = ['pasta','bread','chipe','potatoes','hot chocolate','egg','steak','spaghetti','corn','lollipop']
print(Fore.BLUE,'provinces','colors','countries','animals','animals2','foods','foods2',Fore.RESET)
choise_a = input('select content: ')
if choise_a == 'provinces':
    choise_a = provinces
elif choise_a == 'colors':
    choise_a = colors
elif choise_a == 'countries':
    choise_a = countries
elif choise_a == 'animals':
    choise_a = animals
elif choise_a == 'animals2':
    choise_a = animals2
elif choise_a == 'foods':
    choise_a = foods
elif choise_a == 'foods2':
    choise_a = foods2
answer = random.choice(choise_a)
health = 6
board_game =[]
for i in range(len(answer)):
    board_game.append('_')
A = 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
while True:

    print('')
    print(' '.join(board_game))
    print(health*' ❤')
    print('')
    print(A)

    if ''.join(board_game) == answer:
        print('')
        print(Fore.RED,"YOU WIN 😎",Fore.RESET)
        break

    if health == 0:
        print(Back.WHITE,Fore.BLACK,'"Game over"',Back.RESET,Fore.RESET)
        break

    print('')
    letter = input('enter a letter: ')

    if (letter in answer.upper()) or (letter in answer.lower()):
        idx = answer.index(letter.lower())
        board_game[idx] = letter.lower()
    else:
        health = health - 1