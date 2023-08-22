# map
# یک لیست دارم میخوایم تمامی اجزا یک لیتس یک نمره بهش اضافه کنم یا تمامی اسمامی رو حرف اول رو بزرگ کنم

def plus2 (score):
    return score + 2

scores = [12,17.5,19,25,2523]
new_scores = list(map(plus2,scores))
print(new_scores)

# OCR متن رو از روی عکس در میاره

def check_name(name):
    return name.capitalize()

names = ['hOma','Amir','shahriar','pooria','MOHAMMAD']
new_names = list(map(check_name , names))

print(new_names)