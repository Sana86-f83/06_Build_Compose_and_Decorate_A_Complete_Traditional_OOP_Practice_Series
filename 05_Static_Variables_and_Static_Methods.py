print("\n\t\t","=" * 70)
print("""
\n\t\t\t\t05. Static Variables and Static Methods
\n\t\t\tAssignment:
\t\t\tCreate a class MathUtils with a static method add(a, b)
\t\t\tthat returns the sum. No class or instance variables should be used.
""")

class MathUtils:

    @staticmethod
    def add(a,b):
        return a + b
    
if __name__ == "__main__":

    print("\t\t\tOutput....\n")
    result = MathUtils.add(5,6)
    print("\t\t\t\tSum result -->",result,"\n")    
    print("\t\t","=" * 70,"\n")
