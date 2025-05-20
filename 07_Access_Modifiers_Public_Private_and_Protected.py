# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.


class Employee:
    def __init__(self,name,salary,ssn):
        self.name = name  # public variable
        self._salary = salary  # protected variable
        self.__ssn = ssn  # private variable


if __name__ == "__main__":
    emp = Employee(name="Sana Faisal",salary=50000,ssn="123-45-5457")
    # Access public variable
    print("public variable",emp.name)

    # Access protected variable
    print("protected variable",emp._salary)

    # Access private variable

    try:
        print("private variable",emp.__ssn)

    except AttributeError:
        print("Cannot access private variable __ssn")