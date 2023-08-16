for i in range(9):
    for j in range(6): 
        print(i,j) #چرخدنده ها (مثل)

for i in range(4,9):
    for j in range(3,6): 
        print(i,j) # محدود

for i in range(1,5):
    for x in range(i):
        #وقتی بین حلقه ها وابستگی دارید باید از اندیس حلقه بالا  تر استفاده کنیم
        print(i , end=' ')
    print()#سختاش
    #برنامه نویس یهو به جواب نمیرسیم

for i in range(5): # i در جواب  یک خطه
    if i == 3:
        continue
    for x in range(i+1):
        print(x , end=' ')
    print()#سختاش
#وابستگی حلقه ها به هم یا ن 
# اگه سه چهار تا حلقه باید میزدی بدون شاید کوتاه تر هم بشه