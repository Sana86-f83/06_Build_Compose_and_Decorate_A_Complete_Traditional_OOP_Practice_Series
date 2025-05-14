print("\n\t\t","=" * 70)
print("""
\t\t\t04. Class Variables and Class Methods
\n\t\tAssignment:
\t\tCreate a class Bank with a class variable bank_name. Add a class method \n\t\tchange_bank_name(cls, name) that allows changing the bank name. Show that \n\t\tit affects all instances.
""")

class Bank:
    bank_name = "Habib Bank"

    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name


if __name__ == "__main__":
    print("\t\tOutput....\n")
    obj = Bank()
    print(f"\t\t\tBefore changing Bank name : {obj.bank_name}") 

    Bank.change_bank_name("Allied Bank")
    print(f"\t\t\tAfter changing Bank name : {obj.bank_name}\n")  
    print("\t\t","=" * 70,"\n")
