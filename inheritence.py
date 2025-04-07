#single level inheritence
# Inheritance is a way to form new classes using classes that have already been defined.
# The new class is a specialized version of the old class. The old class is called the base class, and the new class is called the derived class.
#

class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return "same sound"
class Dog(Animal):
    def speak(self):
        return "bark"
dog=Dog("Rockey")
print(dog.name)
print(dog.speak()) # Output: bark 
print("****************************MULTILEVELINHERITENCE***************************************")

# multiple level inheritence
# In multiple inheritance, a class can be derived from more than one base classes.
class  Vehicle:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def move(self):
        return "moving"
class Car(Vehicle):
    def wheels(self):
        return "car has 4 wheels"
class ElectircCar(Car):
    def battery(self):
        return "battery is charging"
    def move(self):
        return "electric car is moving without noise"
car=ElectircCar("Tesla","Red")
print(car.name)
print(car.color)
print(car.wheels())
print(car.battery())
print(car.move()) # Output: electric car is moving without noise
print("************************MULTIPLE INHERITENCE*******************************************")

# multiple inheritence
# In multiple inheritance, a class can be derived from more than one base classes.
class Engine:
    def __init__(self,state):
        self.state=state
    def start(self):
        return "engine is starting"
class vehicle:
    def wheels(self):
        return "vehicle has 4 wheels"
class Car(Engine,vehicle):
    def drive(self):
        return "car is driving"
car=Car("on")
print(car.state)
print(car.start())
print(car.wheels())
print(car.drive()) # Output: car is driving
print("************************HIRECHICHAL INheritance *******************************************")
# multiple inheritence
class Anime:
    def speak(self):
        return "same sound"
class Dog(Anime):
    def speak(self):
        return "Bow Bow"
class Cat(Anime):
    def speak(self):
        return "Meow Meow"
class Cow(Anime):
    def speak(self):
        return "Moo Moo"
dg=Dog()
ct=Cat()
cw=Cow()
print(dg.speak()) # Output: Bow Bow
print(ct.speak()) # Output: Meow Meow
print(cw.speak()) # Output: Moo Moo
print("*******************************************************************")