
print("\n\t\t","=" * 70)
print(f"""\n\t\t\t06. Constructors and Destructors
\n\t\tAssignment:
\t\tCreate a class Logger that prints a message when an object is created 
\t\t(constructor) and another message when it is destroyed (destructor).
""")

class Logger():
        # Constructor
    def __init__(self):
        print("\t\t\tAssalam u ALaikum  ,Object created")
        
        # Destructor
    def __del__(self):
        print("\t\t\tGood bye,object end ")

if __name__ == "__main__":
    print("\t\t\tOutput....\n")
    result = Logger()
    print("\t\t","=" * 70,"\n")
    print("\t\t\tprint end this programm")

