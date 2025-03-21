# Conditional Statements in Python

This section covers conditional statements in Python, including `if`, `if-else`, `if-elif-else`, and nested conditional structures.

## File: [`if-else.py`](https://github.com/ChandraSekharC478/PythonforDevops/blob/main/conditionals/if-else.py)
This script demonstrates the use of conditional statements and logical operators in Python.

## Understanding Conditional Statements
### 1. `if - else` Statement
- If condition:
  - Code body of the `if` statement
- Else:
  - Code body of the `else` statement

### 2. `if-elif-else` Statement
- If condition1:
  - Code block 1 will execute
- Elif condition2:
  - Code block 2 will execute
- Else:
  - Code block 3 will execute

### 3. Nested `if-else`
- If condition1:
  - If condition2:
    - Code block executes if both condition1 and condition2 are True
  - Else:
    - Code block executes if condition1 is True but condition2 is False
- Else:
  - Code block executes if condition1 is False

### 4. Logical Operators with Conditions
- **AND (`and`)**: Both conditions must be True.
  - If number >= 10 and number <= 20:
    - Code will execute if both conditions are true
  - Else:
    - If any of the above conditions is not true
- **OR (`or`)**: At least one condition must be True.
  - If number >= 10 or number <= 20:
    - Code will execute if any of the above conditions is true
  - Else:
    - If any of the above conditions is not true

### 5. Ternary Operator in Python
- Number = 10
  - Result = "Even" if number % 2 == 0 else "Odd"
- Number = -1
  - Result = "Positive" if number > 0 else "Negative" if number < 0 else "Zero"

## Conditional Flow Examples
- Number = 7
  - Result = ("Odd", "Even")[number % 2 == 0]

## Running the Script
To run `if-else.py`, use:
```sh
python if-else.py
```

## GitHub Repository
Explore the full repository here: [Python for DevOps](https://github.com/ChandraSekharC478/PythonforDevops)

Happy Coding! 🚀
