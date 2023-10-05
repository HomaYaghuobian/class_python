class Person:
    def __init__(self,name,age,nationality):
        self.name = name
        self.age = age
        self.nationality = nationality
    def eat(self):
        pass

class Student(Person):
    pass

class At(Student):
    pass