class Employee:
    def __init__(self,name,age,salary):
        self.name=name  #Public modifier
        self.__age=age   #Private modifier
        self._salary=salary #Protected modifier
    def display(self):
        print(f"Name: {self.name}, Age: {self.__age}, Salary: {self._salary}")
employee1=Employee("John",30,50000)
employee1.display()

print(employee1.name)  # Accessing public attribute
print(employee1._salary)  # Accessing protected attribute
#print(employee1.__age)  # Attempting to access private attribute (will raise an error)