class Room:
    length=0.0
    breadth=0.0
    height=0.0

    def caluclate_Area(self):
        area=self.length*self.breadth*self.height
        print(f"The area of the room is: {area}")
livingroom=Room()
livingroom.length=20
livingroom.breadth=15
livingroom.height=10
livingroom.caluclate_Area()
# Key Observations 
# livingroom is an object of class Room
# length, breadth, and height are attributes of the class Room
# We are assigning values to the attributes of the object livingroom
# caluclate_Area() is a method of the class Room
# Output
# The area of the room is: 3000.0