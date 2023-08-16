import random
s_dice = 0
dice = 0

while dice != 6:
    dice = random.randint(1,6)
    print(dice)
    s_dice += dice

print('sum = ',s_dice)