# class Shape:
#     def _init_(self,length,breadth,radius):
#         self.length=length
#         self.breadth=breadth
#         self.radius=radius
#     def  rectangle_area(self):
#         area=self.length*self.breadth
#         print(f"The area of the rectangle is: {area}")
#     def circle_area(self):
#         area=3.14*self.radius*self.radius
#         print(f"The area of the circle is: {area}")
#     def square_area(self):
#            area=self.length*self.length
#         print(f"The area of the square is: {area}")
# shape1=Shape()
# shape1._init_(20,10,10)
# shape1.rectangle_area()
# shape1.circle_area()    
# shape1.square_area()
class Shape:
    def __init__(self, length, breadth, radius): # Constructor of the class
        self.length = length
        self.breadth = breadth
        self.radius = radius

    def area_rectangle(self):       # Method to calculate the area of a rectangle
        return self.length * self.breadth

    def area_square(self):          # Method to calculate the area of a square
        return self.length * self.length

    def area_circle(self):      # Method to calculate the area of a circle
        return 3.14 * self.radius * self.radius

    def display_areas(self):    # Method to display the areas of rectangle, square, and circle
        print(f"Area of Rectangle: {self.area_rectangle()}")
        print(f"Area of Square: {self.area_square()}")
        print(f"Area of Circle: {self.area_circle()}")

# Creating an instance of Shape
shape1 = Shape(10, 20, 5)
shape1.display_areas()
# Key Observations
# __init__() is a constructor of the class Shape
# area_rectangle(), area_square(), and area_circle() are methods of the class Shape
# display_areas() is a method of the class Shape
# shape1 is an object of class Shape
# Output
# Area of Rectangle: 200
# Area of Square: 100
# Area of Circle: 78.5

        