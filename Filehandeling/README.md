# 📁 Python File Handling Practice

This project showcases various file handling operations in Python using the built-in `os` module and standard file I/O techniques.

---

## 📂 Directory Management

### ✔️ Get Current Working Directory
```python
import os
print(os.getcwd())
```

### ✔️ Change Directory
```python
os.chdir('C://Users//Chandrasekhar//OneDrive//Desktop//Python-scripting//Filehandeling')
```

---

## 📝 File Writing and Reading

### ✔️ Write Product Details to a File
```python
Product_List = [
    'Name: Laptop\n',
    'Brand: HP\n',
    'Model: HP Pavilion 15\n',
    'Price: 50000\n'
]

with open('Product_List.txt', 'w') as file:
    file.writelines(Product_List)
```

### ✔️ Read File Content
```python
with open('Product_List.txt', 'r') as file:
    print(file.read().strip())
```

---

## 📄 File Copy, Rename, Delete, and Restore

### ✔️ Copy File Content
```python
with open('product_info.txt', 'r') as src, open('product_info_copy.txt', 'w') as dest:
    dest.write(src.read())
```

### ✔️ Rename the File
```python
os.rename('product_info_copy.txt', 'product_info_backup.txt')
```

### ✔️ Remove the Original File
```python
os.remove('product_info.txt')
```

### ✔️ Restore Backup to New File
```python
with open('product_info_backup.txt', 'r') as src, open('final_product_info.txt', 'w') as dest:
    dest.write(src.read())
```

---

## 🖋️ Append and Read Back

### ✔️ Append to a File
```python
with open('write_demo_file.txt', 'a') as file:
    file.write("\nThis is the appended content.")
```

### ✔️ Read After Appending
```python
with open('write_demo_file.txt', 'r') as file:
    print(file.read())
```

---

## 📖 Reading Techniques

### ✔️ Read Entire File
```python
with open('sales.txt', 'r') as fp:
    print(fp.read())
```

### ✔️ Read First Line
```python
def read_first_line(file_path):
    with open(file_path, 'r') as file:
        return file.readline().strip()
```

### ✔️ Read All Lines
```python
def read_all_lines(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()
```

### ✔️ Read First 4 Lines
```python
def first_four_lines(file_path):
    with open(file_path, 'r') as file:
        for i in range(4):
            print(file.readline().strip())
```

### ✔️ Read First and Last Line
```python
def first_and_last_line(file_path):
    with open(file_path, 'r') as file:
        first_line = file.readline().strip()
        for line in file:
            pass
        last_line = line.strip()
        print("First line:", first_line)
        print("Last line:", last_line)
```

---

## 🧰 Tools Used

- Python 3.x
- Built-in `os` module
- Standard I/O operations

---

## 👨‍💻 Author

**Chandrasekhar**

Practicing and mastering Python file handling through structured and practical use cases.