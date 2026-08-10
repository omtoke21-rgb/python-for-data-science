# Classes and Objects

class Student:

    def __init__(self, name, branch, year):
        self.name = name
        self.branch = branch
        self.year = year

    def display(self):
        print("Name:", self.name)
        print("Branch:", self.branch)
        print("Year:", self.year)


student = Student("Arjun", "AI&DS", 3)

student.display()
