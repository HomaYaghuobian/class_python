s = "aaaaaaaaaaaahrtbfhbs;mtmdmboerhn'aemklfnba;berh"
d = {}
for letter in s:
    if letter not in d:
        d[letter] = 1
    else:
        d[letter] += 1
    # print(d)
print(d)






# اگر دو تا کلید یکسان با متغیر متفاوت داشته باشیم،یکی ش رو حتما میگه اخریه رو نشون میده
# اگر کلید ها متفاوت ولی متغیر ها یکسان مهم نیست جفتش رو نشون میده