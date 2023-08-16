import random
# randint
random_num = random.randint(0,10) # اعداد رندم از اول اون عدد اول هست تا اخر اون عدد دومی که وارد میکنیم
print(random_num)
#random
a = random.random() #با حداکثر عدد اعشار بین صفر و یک 
print(a)
#choice
names = ['homa','mohammad','sina','navidreza','pooria'
        'sadra','shariar']
lucky_name = random.choice(names)
print(lucky_name)
# choices
names = ['homa','mohammad','sina','navidreza','pooria'
        'sadra','shariar']
# سرچ ، تکراری نمیاره