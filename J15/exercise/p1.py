# public , private , protected

class Person:
    def __init__(self,name,age):
        self.__name = name # private (کلا خصوصی)
        self._age = age   # protected (در دسترس نیست مگر در کلاس فرزند)
        self.weight , self.height = 0 , 0

    def set_bodyinfo(self,w,h):
        self.weight = w
        self.height = h
    
    def show_info(self):
        self.__name 
        print(f'Hi, My name is {self.name}') # چون خصوصیه نمیاره
        print(f'I am {self._age}.')
        print(f'WEIGHT= {self.weight} ||| HEIGHT= {self.height}')

class Student(Person):
    pass

stu1 = Student('ali', '25')
stu1.set_bodyinfo(80,180)
stu1.show_info()
# public
