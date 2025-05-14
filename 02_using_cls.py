print("\n\t\t","=" * 60)
print(f"""
\t\t\t\t-Using cls:
\t\t-Assignment_2:
\t\tCreate a class Counter that keeps track of how many 
\t\tobjects have been created.Use a class variable and a 
\t\tclass method with cls to manage and display the count.\n""")

class Counter:
    count = 0  # class variable

    def __init__(self):
        Counter.count += 1  # jab bhi new object banay, count barhao

    @classmethod
    def show_count(cls):  # class method to show the count
        print("\t\tOutput.....")
        print(f"\t\t\tTotal objects created: {cls.count}")
        print("\t\t","=" * 60)

# Create 3 objects
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

# Show how many objects created
Counter.show_count()

# =======================================End
