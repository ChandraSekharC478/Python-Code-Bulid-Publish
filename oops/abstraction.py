from abc import ABC, abstractmethod        # we are importing the module ABC(Abstract Base Classes)

class Product(ABC):
    
    @abstractmethod
    def display_product_info(self):
        pass
    
    @abstractmethod
    def calculate_price(self):
        pass
    
#ssince the beow class PhysicalProduct is not overrding he 2nd method "calcualte_price" so as per the concept of abstraction
# this class also becomes abstrct in nature and we cant create the object of this class now
class PhysicalProduct(Product):
    def __init__(self, name ,price, weight):
        self.name = name
        self.price = price
        self.weight = weight
        
    def display_product_info(self):           # method overriding
        print(f"Product with name : {self.name} is having the weight of {self.weight} kg")
    
    '''def calculate_price(self):
       shipping_cost = self.weight * 10    # so suppose we have 10/- per kg
       total_price = shipping_cost + self.price
       print(f"total_price of the product is {total_price}")'''
       
       
# The below class is sub class of the PhysicalProduct class and providing the method overrdiing of the left over abstaract method
# os we can use this class to create the object now
class Electronics(PhysicalProduct):   
    
    def calculate_price(self):
       shipping_cost = self.weight * 10    # so suppose we have 10/- per kg
       total_price = shipping_cost + self.price
       print(f"total_price of the product is {total_price}")
    
laptop = Electronics("Laptop", 40000, 3)
laptop.display_product_info()
laptop.calculate_price()