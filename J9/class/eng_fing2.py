mydict = {
    "apple" : "sib",
    "I" : "man",
    "car" : "mashin",
    "cat" : "grobe",
    "coler" : "rang",
    "hi" : "salam"
}
s = input('Enter the sentence')
answer = []
l = s.split()
for word in l : 
    if word in mydict :  # کلید ها (کی) ها رو استفاده میکنه
        answer.append(mydict[word])  #هرچی سمت چپه کلیده 
    else:
        answer.append(word)
print(''.join(answer))   # پنجره با دو نقطه. یکم صبر کن میاد