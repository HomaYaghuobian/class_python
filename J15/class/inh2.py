# Inheritance - ارث بری
# تمامی ویژگی های پدرم رو ارث ببرم.. من دانشجو م و پدر م میشه انسان
# بعد حالا که دانشجو ام انسان هستم ولی یک ویژگی هایی بهم اضافه شده و فرزند دانشجو مثلا ثبت در هییت علمی هستیم که خودش ویژگی ها داره
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.weight , self.height = 0 , 0

    def set_bodyinfo(self,w,h):
        self.weight = w
        self.height = h
    
    def show_info(self):
        print(f'Hi, My name is {self.name}')
        print(f'I am {self.age}.')
        print(f'WEIGHT= {self.weight} ||| HEIGHT= {self.height}')

class Student(Person):
    pass

stu1 = Student('ali', '25')
stu1.set_bodyinfo(80,180)
stu1.show_info()