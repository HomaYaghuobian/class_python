# نتیجه رو توی فایلی ذخیره میکنیم که ذخیره میشه در سیستم.کد معنا پیدا میکنه

# open - close  باز و بسته کردن فایل
# read - write  میخونه یا مینویسه کل متن رو میاره بیرون رو میده بهت
# readlines - writelines خط خط میده بهت تا اون پیرینته

# -    dash


f = open('J12\class\scores.txt','r')
mydata = f.read()

scores = mydata.split(' - ')
for score in mydata:
    print(score)

print(mydata)

f.close()

# f = open('J12\class\scores.txt','r')
# mydata = f.readline()
# print(mydata)
# f.close()