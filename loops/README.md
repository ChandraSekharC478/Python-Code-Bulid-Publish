# Python for DevOps - Loops in Python

This section covers loops in Python, including `for` loops, iterating over sequences, using the `range()` function, conditional logic within loops, and special loop control statements like `break` and `continue`.

## Understanding Loops
### 1. `for` Loop
- Iterates over a sequence (list, string, range, etc.).

### 2. Iterating Through a String
- Loops through characters of a string.

### 3. Using `range()` in Loops
- Generates a sequence of numbers for iteration.

### 4. Conditional Statements in Loops
- Combining loops with `if` conditions to filter values.

### 5. Storing Even and Odd Numbers in Lists
- Using lists to store categorized numbers during iteration.

### 6. `break` and `continue` Statements
- `break`: Exits the loop when a condition is met.
- `continue`: Skips the current iteration and continues with the next one.

## Code Snippets
```python
# For Loops 
languages = ['Java', 'Js', 'Python', 'C', 'C++', 'Ruby', 'Node Js']
for a in languages:
    print(a)
print("*************************************************")

# Iterating through a string
hobby = 'PlayingCricket'
for b in hobby:
    print(b)
print("*************************************************")

# Range function in for loop
for i in range(1, 10):
    print(i)
print("*************************************")

# Loop with Conditional Statements
for i in range(1, 10):
    if i % 2 == 0:
        print(f'{i} is even')
        print("********")
    else:
        print(f'{i} is odd')
        print("********")
print("************************************")

# Printing odd and even numbers in separate lists
Even = []  # Empty even list
Odd = []   # Empty odd list
for i in range(1, 20):
    if i % 2 == 0:
        Even.append(i)
    else:
        Odd.append(i)
print("Even numbers:", Even)
print("Odd numbers:", Odd)
print("************************")

# Break and Continue Statements
for a in languages:
    if a == 'Js':
        break  # Breaks loop execution if condition is met
    print(a)

print("************************")

# Continue - Skips the matched condition and continues
for a in languages:
    if a == "C++":
        continue
    print("Continue statement:", a)
```

## Running the Script
To run the script, use:
```sh
python loops.py
```

## Key Takeaways
- Loops help automate repetitive tasks.
- The `for` loop can iterate over lists, strings, and sequences.
- `range()` generates sequences of numbers.
- Conditional statements inside loops help filter values.
- `break` stops loop execution, while `continue` skips the current iteration.

## GitHub Repository
Explore the full repository here: [Python for DevOps](https://github.com/ChandraSekharC478/PythonforDevops)

Happy Coding! 🚀