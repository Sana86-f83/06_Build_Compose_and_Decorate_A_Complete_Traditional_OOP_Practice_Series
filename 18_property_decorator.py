# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self,price):
        self._price = price

    @property
    def price(self):
        try:
            return self._price 
        
        except AttributeError:
            return "price value deleted"      

    @price.setter
    def price(self,newPrice):
        self._price =  newPrice

    @price.deleter
    def price(self):
        del self._price
        print("Deleted price ")

# Testing
obj = Product(300)
print("Before price ",obj.price)  
obj.price = 400  
print("After price",obj.price)
del obj.price
print(obj.price)