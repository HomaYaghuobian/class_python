def word(a):
    u , l = 0 , 0

    for letter in a:
        if letter.isupper():
            u += 1
        elif letter.islower():
            l += 1
    return u , l 

u , l = word('Alireza')
print(f'Upper letter: {u}, Lower letter: {l}')