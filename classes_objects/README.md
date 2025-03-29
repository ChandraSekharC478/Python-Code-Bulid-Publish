# Python for DevOps - Classes and Objects

This section covers object-oriented programming (OOP) concepts in Python, including classes, objects, constructors, and methods.

## Understanding Classes and Objects
### 1. What is a Class?
- A class is a blueprint for creating objects. It defines attributes (variables) and behaviors (methods).

### 2. What is an Object?
- An object is an instance of a class. It contains the data and methods defined in the class.

## Example: Shape Class
```python
class Shape:
    def __init__(self, length, breadth, radius):  # Constructor
        self.length = length
        self.breadth = breadth
        self.radius = radius

    def area_rectangle(self):  # Method to calculate rectangle area
        return self.length * self.breadth

    def area_square(self):  # Method to calculate square area
        return self.length * self.length

    def area_circle(self):  # Method to calculate circle area
        return 3.14 * self.radius * self.radius

    def display_areas(self):  # Method to display all areas
        print(f"Area of Rectangle: {self.area_rectangle()}")
        print(f"Area of Square: {self.area_square()}")
        print(f"Area of Circle: {self.area_circle()}")

# Creating an object of Shape class
shape1 = Shape(10, 20, 5)
shape1.display_areas()
```

## Key Observations
- `__init__()` is a **constructor** that initializes object attributes.
- `area_rectangle()`, `area_square()`, and `area_circle()` are **methods** that perform calculations.
- `display_areas()` is a **method** that prints calculated areas.
- `shape1` is an **object** of class `Shape`.

## Output
```
Area of Rectangle: 200
Area of Square: 100
Area of Circle: 78.5
```

## Running the Script
To execute the class script, use:
```sh
python classes_objects.py
```

## Why Use Classes in DevOps?
- **Encapsulation:** Groups related functions and data.
- **Reusability:** Write once, reuse multiple times.
- **Scalability:** Helps in managing automation workflows and cloud infrastructure efficiently.

## GitHub Repository
Explore the full repository here: [Python for DevOps](https://github.com/ChandraSekharC478/PythonforDevops)

Happy Coding! 🚀

