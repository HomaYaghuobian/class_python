import random
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.weight , self.height = 0 , 0
        print('Person Initialization')

    def set_bodyinfo(self,w,h):
        self.weight = w
        self.height = h
    
    def show_info(self):
        print(f'Hi, My name is {self.name}')
        print(f'I am {self.age}.')
        print(f'WEIGHT= {self.weight} ||| HEIGHT= {self.height}')

class Student(Person):
    # Overwriting - بازنویسی
    def __init__(self , name , age , konkor , past_average):
        # Person.__init__(self,name,age) #کار تکراری نباید انجام بدی
        super().__init__(name,age)  # سوپر کار سلف رو انجام میده و مال پرسنه
        
        self.rank = konkor
        self.pre_average = past_average
        print('Studnet Initialization')
    def create_id(self):
        self.id = random.randint(14000,20000)

    def set_average(self,avg):
        self.average = avg

    def welcome(self):
        print(f'Hi i am a student and my name is {self.name} and my id is {self.id}')
# stu1 = Student('ali', '25')
# stu1.set_bodyinfo(80,180)
# stu1.show_info()
stu1 = Student('ali', 18 , 110 ,19.54)
stu1.set_bodyinfo(80,180)
stu1.show_info()

print('#' * 20)

stu1.create_id()
stu1.set_average(13.90)
stu1.welcome()

print('#' * 20)

p1 = Person('taha' , 30 )
p1.show_info()