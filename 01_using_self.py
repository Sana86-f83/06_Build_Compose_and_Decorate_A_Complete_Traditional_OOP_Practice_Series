
print("\n","*" * 40)
print(f"""
. Using self
. Assignment_1:
. Create a class Student with attributes name and marks. 
. Use the self keyword - to initialize these values via a constructor. 
. Add a method display() that prints student details.
""")

class Student:
    def __init__(self, name, marks):
        self.name = name        # using self to assign the name
        self.marks = marks      # using self to assign the marks

    def display(self):
        print("\n","*" * 40)
        print("\tStudent Name:", self.name)
        print("\tStudent Marks:", self.marks)
        print("\n","*" * 40)

if __name__  == "__main__":
    student1 = Student("Ali", 87)
    student1.display()

# =================================End