print(f"""
. Using self
. Assignment:
. Create a class Student with attributes name and marks. 
. Use the self keyword - to initialize these values via a constructor. 
. Add a method display() that prints student details.
""")

class Student:
    def __init__(self, name, marks):
        self.name = name        # using self to assign the name
        self.marks = marks      # using self to assign the marks

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)

student1 = Student("Ali", 87)
student1.display()

