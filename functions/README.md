# Python for DevOps - Functions in Python

This section covers functions in Python, including function definitions, parameters, return values, and real-world applications.

## Understanding Functions
### 1. Function Definition & Calling
- Functions help break code into reusable blocks.
- Defined using the `def` keyword.

```python
# Function Definition
def display():
    print("We are calling the function")

# Function Call
display()
```

### 2. Function with One Parameter
- Parameters allow passing values to functions.

```python
def printName(name):
    print("My name is:", name)

printName("Chandra")
```

### 3. Function with Multiple Parameters
- Functions can take multiple parameters.

```python
a = 10
b = 20
c = 30

def calculate(a, b, c):
    sum = a + b + c
    print(sum)

calculate(a, b, c)
```

### 4. Returning Values from Functions
- Functions can return computed values.

```python
def sum(a, b):
    return a + b  # Returning the sum

y = sum(a, b)
print("Sum of two numbers is:", y)
print("Product of the sum is:", y * y)
```

### 5. Function Assignments
- **Calculate Simple Interest**
  - Formula: `SI = P * R * T / 100`

```python
principle = 1000
rate = 10
time = 2

def simpleInterest(principle, rate, time):
    return (principle * rate * time) / 100

print("Simple Interest is:", simpleInterest(principle, rate, time))
```

- **Calculate Total Amount with Interest**
  - Formula: `A = P + SI`

```python
amount = principle + simpleInterest(principle, rate, time)
print("Total Amount is:", amount)
```

## Running the Script
To run the functions script, use:
```sh
python functions.py
```

## Key Takeaways
- Functions help modularize and reuse code.
- Parameters allow flexibility in function execution.
- Functions can return values to the caller.
- Real-world applications include financial calculations.

## GitHub Repository
Explore the full repository here: [Python for DevOps](https://github.com/ChandraSekharC478/PythonforDevops)

Happy Coding! 🚀

