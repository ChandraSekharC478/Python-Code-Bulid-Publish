class Calculator:
    def add(self,a=2,b=1,c=1): # default values for  a,b and c
        # This method can take 1, 2 or 3 arguments
        return a+b+c 
object1=Calculator() # creating the object of the class
# calling the method with different number of arguments


print(object1.add(10)) # calling the method with 1 argument
print(object1.add(10,20)) # calling the method with 2 arguments
print(object1.add(10,20,30)) # calling the method with 3 arguments
# The output of the above code will be:
# 12
# 31
# 60
# The concept of polymorphism allows us to use the same method name with different number of arguments.