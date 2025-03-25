# if the function is defined inside another function, then it is called a nested function.
# Nested functions can access variables of the enclosing scope. 


def outerfunctext():
    def innerfunc():
        print("This is inner function")
    print("This is outer function")
    innerfunc()
outerfunctext()

print("**********************")
# Nested functions can access variables of the enclosing scope.
# In the below example, the inner function can access the variable name of the outer function.
# The inner function can modify the value of the variable name of the outer function.
# The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.
# Use the nonlocal keyword to declare that the variable is not local.
# If we change the value of a nonlocal variable, the changes appear in the local variable.
# The nonlocal keyword is used to work with the variable of the outer function, not the global variable.
# 
def outerfunc():
    name="local_name"  # these are the local variables
    age=30
    def innerfunc():
        nonlocal name 
        name= "non_local_name" # these are the nonlocal variables
        age=25                         # these are the local variables
        print("This is inner function")
        print("the inner function name is:",name)  # it will print the value of the nonlocal variable
        print("The inner  function age is:",age)    # it will print the value of the local variable and over ride the value of the outer function age=40
    print("This is outer function")
    print("The outer function name is:",name) # it will print the value of the local variable
    print("The outer function age is:",age)   # it will print the value of the local variable
    innerfunc()
outerfunc()

# in the above code first outer function will be call it will go inside the outer function and it will print the value of the local variable name and age
# then it will call the inner function and it will print the value of the nonlocal variable name and local variable age 
# and it will print the value of the nonlocal variable name and local variable age
# Output:
# This is outer function
# The outer function name is: local_name    
# The outer function age is: 30
# This is inner function
# the inner function name is: non_local_name
# The inner  function age is: 25
# **********************

