# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self,name,breed):
        self.name = name   #instance variable
        self.breed = breed  #instance variable

    def bark(self):   #instance method
        print(f"{self.name} is barking!")    

if __name__ == "__main__":
    # creating an object instance
    my_dog = Dog("Tommy","Labrador") 
    
    # call the method
    my_dog.bark()