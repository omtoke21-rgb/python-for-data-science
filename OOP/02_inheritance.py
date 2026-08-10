# Inheritance

class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)


class Student(Person):

    def study(self):
        print(self.name, "is studying Data Science.")


student = Student("Om")

student.introduce()
student.study()
