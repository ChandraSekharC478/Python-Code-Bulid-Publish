
# 🧾 Employee Data JSON Handler

This Python script demonstrates how to handle JSON files using Python's built-in `json` and `os` modules. It performs basic file handling operations such as creating, writing, and reading structured employee data from a JSON file.

---

## 📁 Directory Setup

Before running the script, ensure the following directory exists:

```
C://Users//Chandrasekhar//OneDrive//Desktop//Python-scripting//Filehandeling
```

This is where the script will read/write the `employee.json` file.

---

## 🛠 Features

- Create a list of employee dictionaries
- Serialize and save the data to a JSON file
- Deserialize and read data from the JSON file
- Display data in a formatted way using a loop

---

## 🧾 Sample JSON Structure

Here's a snippet of what the `employee.json` file will look like:

```json
[
    {
        "id": "EMP001",
        "name": "Chandrasekhar R",
        "department": "Engineering",
        "role": "Frontend Developer",
        "email": "chandrasekhar.r@example.com",
        "phone": "+91-9876543210",
        "location": "Hyderabad"
    },
    {
        "id": "EMP002",
        "name": "Ananya Sharma",
        "department": "Marketing",
        "role": "Digital Marketing Specialist",
        "email": "ananya.sharma@example.com",
        "phone": "+91-9988776655",
        "location": "Bangalore"
    }
]
```

---

## 📜 Python Snippets

### ✅ Writing JSON to File

```python
with open('employee.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
```

### ✅ Reading JSON from File

```python
with open('employee.json', 'r') as json_file:
    data = json.load(json_file)
    for emp in data:
        print(f"Name: {emp['name']} - Role: {emp['role']}")
```

---

## 🖥 Output Example

```text
ID: EMP001
Name: Chandrasekhar R
Department: Engineering
Role: Frontend Developer
Email: chandrasekhar.r@example.com
Phone: +91-9876543210
Location: Hyderabad
------------------------------
```

---

## 🚀 How to Run

Make sure you have Python 3 installed. Then, simply run the script:

```bash
python employee_script.py
```

---

## 📦 Requirements

- Python 3.x
- No external libraries required

---

## 👨‍💻 Author

**Chandrasekhar R**  
DevOps Engineer | Banglore , India  
📧 chandrasekharc784@gmail.com

---

## 📌 Optional Enhancements

- Add employee data via user input
- Update or delete specific employee records
- Export employee data in CSV format
- Integrate with a REST API
