# Block of code we are writing the code to perform some specific tasks
# syntax:
# def name_of_function():
#   // block of the code
# name_of_function()

def display():
    print("we are calling the function")
display()
print("********************")

# function with one Parameter
def printName(name):
    print("my name is:",name)

printName("chandra")

print("**********************")
# function with two  or Parameters
a=10
b=20   # these are the Global variables
c=30

def caluclate(a,b,c):
    sum=a+b+c   # these are the local Variables
    print(sum)

caluclate(a,b,c)

print("**********************")

# Return value from the function 

def sum(a,b):
    return a+b;   # return the value to the calling function

y=sum(a,b);  # calling the function here we get the value fromm the function i.e. sum=10+20=30
print("sum of two numbers is:",y) # printing the value
print("product of the the sum  is:",y*y) # printing the value

print("**********************")

# Assignment for the functions
# 1. write a function to calculate the simple interest  i.e. SI= P*R*T/100
# 2. write a function to calculate the  total Amount  with interest i.e. A=P+SI
principle=1000
rate=10
time=2
def simpleInterest(principle,rate,time):
    SI=(principle*rate*time)/100
    return SI
amount=principle+simpleInterest(principle,rate,time)
print("Simple Interest is:",simpleInterest(principle,rate,time))
print("Amount is:",amount)