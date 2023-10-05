class Person:
    def __init__(self,name,age,nationality,gender):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.gender = gender
    def eat(self):
        pass
    def sleep(self):
        pass
    def to_live(self):
        pass
    def laughing(self):
        pass

class Student(Person):
    def study(self):
        pass
    def answering_the_lesson(self):
        pass

class At(Student):
    def helping_students(self):
        pass
    