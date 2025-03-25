# Nested Functions in Python

## Introduction
In Python, if a function is defined inside another function, it is called a **nested function**. Nested functions allow access to variables of the enclosing function's scope.

### Key Points:
- Nested functions can access variables of their enclosing scope.
- The `nonlocal` keyword allows modifying a variable from the outer function.
- Local and nonlocal variables behave differently within nested functions.

## Example 1: Basic Nested Function

```python
def outerfunctext():
    def innerfunc():
        print("This is inner function")
    print("This is outer function")
    innerfunc()

outerfunctext()
```
### Output:
```
This is outer function
This is inner function
```

## Example 2: Accessing Variables from the Outer Function

```python
def outerfunc():
    name = "local_name"  # Local variable
    age = 30
    
    def innerfunc():
        nonlocal name  # Nonlocal variable
        name = "non_local_name"  # Modifying the outer function variable
        age = 25  # Local variable within inner function
        print("This is inner function")
        print("The inner function name is:", name)  # Prints nonlocal variable
        print("The inner function age is:", age)  # Prints local variable of inner function

    print("This is outer function")
    print("The outer function name is:", name)  # Prints local variable before modification
    print("The outer function age is:", age)  # Prints local variable before modification
    innerfunc()

outerfunc()
```
### Output:
```
This is outer function
The outer function name is: local_name
The outer function age is: 30
This is inner function
The inner function name is: non_local_name
The inner function age is: 25
```

## Explanation:
1. The **outer function** is called first, printing its local variable values.
2. The **inner function** is called within the outer function.
3. The inner function modifies the `name` variable using `nonlocal`, but `age` remains local to the inner function.
4. Changes to the `nonlocal` variable reflect in the outer function, but changes to local variables do not affect the outer function.

## Conclusion:
- **Nested functions** help in data encapsulation and better organization of code.
- **`nonlocal` keyword** allows modifying outer function variables inside the inner function.
- **Local variables** of the inner function do not affect the outer function's scope.

This concept is widely used in closures and decorators in Python.

---
## GitHub Repository
Explore the full repository here: [Python for DevOps](https://github.com/ChandraSekharC478/PythonforDevops)

Happy Coding! 🚀

