def new_word(word,letter):
    word = word.split(letter)
    new_word = '!'.join(word)
    return new_word

def New_word(word):
    s = ['a','e','i','o','u']
    for letter in s:
        word = new_word(word,letter)
    return word

word = input('enter your word: ')
answer = New_word(word)

print(answer)