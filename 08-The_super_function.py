# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

# Step1: Parent class
class Person:
    def __init__(self,name):
        self.name = name

# Step2: Child class
class Teacher(Person):  #inheriting person
    def __init__(self,name,subject):
        super().__init__(name) 
        self.subject = subject

    def display(self):
        print(f"Teacher name : {self.name}, Subject : {self.subject}")          

if __name__ == "__main__":
    teacher = Teacher("miss shanzay","python")
    print(teacher.name,teacher.subject)        