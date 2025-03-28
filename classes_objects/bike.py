class Bike :
    name=""
    wheel=2
    gear=4
    brand=""
bike11=Bike()
bike2=Bike()
bike11.name="Yamaha Mountain"  # we are assigning the value to the object
bike11.brand="Yamaha"

print(bike11.name)
print(bike11.brand)
print(f"Number of wheels in the bike: {bike11.wheel}, Number of gears in the bike: {bike11.gear}, Brand of the bike: {bike11.brand},bike name: {bike11.name}")
# Key Observations 
# bike11 is an object of class Bike
# name and brand are attributes of the class Bike
# We are assigning values to the attributes of the object bike11
bike2.name="Honda Mountain"  # we are assigning the value to the object
bike2.brand="Honda"
bike2.gear=5
bike2.wheel=3
print(f"Number of wheels in the bike: {bike2.wheel}, Number of gears in the bike: {bike2.gear}, Brand of the bike: {bike2.brand},bike name: {bike2.name}")