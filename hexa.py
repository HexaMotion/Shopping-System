#Shopping System with Inheritance in Python

class Product:
    def __init__(self, name, price):
        self.name=name
        self.price=price
    
    def details(self):
        print (f"Your product name is {self.name} and it's price is ${self.price}.")
# Derived classes
class Electronics (Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty=warranty
    
    def details(self):   
        print (f"The warranty of your product is {self.warranty} years.")  
# Derived classes
class Clothing (Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size=size
    
    def details(self):
        print (f"The size of your product is {self.size} lit.")
# Derived classes
class Book(Product):
    def __init__(self, name, price, author):
        super().__init__(name, price)
        self.author = author
    
    def details(self):    
        print (f"The author of your product is {self.author}.") 

# Example usage
if __name__ == "__main__":
    p1 = Electronics("Laptop", 20000, 3)
    p2 = Clothing("T-shirt", 200,1)
    p3 = Book("Cracking the Coding Interview",800,"Gayle Laakmann McDowell")
# Display details   
    print("\n--- Electronics ---")
    p1.details()

    print("\n--- Clothing ---")
    p2.details()

    print("\n--- Book ---")
    p3.details()
#run: python this file.py
