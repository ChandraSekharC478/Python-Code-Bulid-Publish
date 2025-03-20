# Python Data Types

This repository contains Python scripts demonstrating different types of data types in Python, including primitive and non-primitive data types.

## Files Overview

### 1. [variables.py](https://github.com/ChandraSekharC478/PythonforDevops/blob/main/variables/variables.py)
This script covers the concept of variables in Python, which act as containers to store data.

**Example Variables:**
```python
emp_name = "chandhu"
emp_age = 40
city = "Tirupati"
print(emp_name, emp_age, city)
print(emp_age)
print(city)
```

### 2. [premitivedatatypes.py](https://github.com/ChandraSekharC478/PythonforDevops/blob/main/variables/primitive_dataTypes.py)
This script demonstrates primitive data types in Python, including Numbers, Strings, and Floats.

**Key Concepts:**
- Integer operations
- String concatenation
- Float arithmetic
- Type checking using `type()`

**Example Output:**
```sh
5
15
***************
chandhu
sekharchandhu
*******************
1.5
16.5
********************
<class 'str'>
<class 'float'>
<class 'int'>
```

### 3.[nonpremitivedatatypes.py](https://github.com/ChandraSekharC478/PythonforDevops/blob/main/variables/nonprimitivedatatypes.py)
This script explains non-primitive data types, which are mutable in nature. It includes Lists, Tuples, and Dictionaries.

**Key Concepts:**
- **Lists**: Mutable, supports indexing, updating, and appending.
- **Tuples**: Immutable.
- **Dictionaries**: Key-value pairs, supports updates and nested structures.

**Example:**
```python
# List Example
fruits = ['Apple','Mango','jackFruit','Banana']
print(fruits)
fruits[2] = 40
fruits.append(56)
print(fruits)
```

```python
# Dictionary Example
students = {"name":"chandhu", "surname":"Kanna", "age":"26", "rollnumber":24}
students.update({"pincode": 12345})
print(students)
```

## Running the Scripts
To execute any of the scripts, run the following command:
```sh
python filename.py
```
Example:
```sh
python variables.py
```

## GitHub Repository
The scripts are part of the [Python for DevOps](https://github.com/ChandraSekharC478/PythonforDevops/blob/main/variables/variables.py) repository.

Feel free to explore and contribute! 🚀
