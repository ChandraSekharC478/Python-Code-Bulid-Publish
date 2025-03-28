#Create a class Student with attributes name, age, and marks. Add a method get_grade() that returns a grade based on marks.
class Student:
    def __init__(self, name, age, marks):  # Corrected __init_method __
        self.name = name
        self.age = age
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        else:
            return "F"

# Creating a Student object
student1 = Student("Chandra", 25, 85)

# Printing student details and grade
print(f"Name: {student1.name}, Age: {student1.age}, Marks: {student1.marks}, Grade: {student1.get_grade()}")
