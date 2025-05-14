print("\n\t\t","=" * 60)
print('''\n\t\t\t\t03_Public Variables and Methods
\t\tAssignment:
\t\tCreate a class Car with a public 
\t\tvariable brand and a public method start(). 
\t\tInstantiate the class and access both from outside the class.
''')

class Car:
    def __init__(self,brand):
        self.brand = brand

    def start(self):
        print(f"\t\t\t{self.brand} is started...")

if __name__ == "__main__":
    myCar = Car("Honda")
    print("\t\tOutput.....")

    # print public variable
    print(f"\t\t\t{myCar.brand}")

    # print public method
    myCar.start()            
    print("\t\t","=" * 60,"\n")
