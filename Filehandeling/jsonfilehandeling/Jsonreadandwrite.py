import json
import os
# data={
#   "id": "EMP001",
#   "name": "Chandrasekhar R",
#   "department": "Engineering",
#   "role": "Devops Engineer",
#   "email": "chandrasekhar.r@example.com",
#   "phone": "+91-9876543210",
#   "location": "Hyderabad"
# }
data= [
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
    },
    {
      "id": "EMP003",
      "name": "Ravi Kumar",
      "department": "Human Resources",
      "role": "HR Manager",
      "email": "ravi.kumar@example.com",
      "phone": "+91-9123456789",
      "location": "Delhi"
    },
    {
      "id": "EMP004",
      "name": "Sneha Patil",
      "department": "Finance",
      "role": "Financial Analyst",
      "email": "sneha.patil@example.com",
      "phone": "+91-9090909090",
      "location": "Pune"
    },
    {
      "id": "EMP005",
      "name": "Arjun Mehta",
      "department": "Product",
      "role": "Product Manager",
      "email": "arjun.mehta@example.com",
      "phone": "+91-9988001122",
      "location": "Chennai"
    }
  ]


print(os.getcwd() )# get current working directory
os.chdir('C://Users//Chandrasekhar//OneDrive//Desktop//Python-scripting//Filehandeling')# to change the directory

with open('employee.json', 'w') as json_file:
    json.dump(data,json_file,indent=4) # write the content in the file
# read the content of the file
# with open('employee.json', 'r') as json_file:
#     data = json.load(json_file) # read the content of the file
#     print(data) # print the content of the file
with open('employee.json', 'r') as json_file:
    data = json.load(json_file) # read the content of the file
    for emp in data:
        print(f"ID: {emp['id']}")
        print(f"Name: {emp['name']}")
        print(f"Department: {emp['department']}")
        print(f"Role: {emp['role']}")
        print(f"Email: {emp['email']}")
        print(f"Phone: {emp['phone']}")
        print(f"Location: {emp['location']}")
        print("-" * 30)  # Separator between employees
print(data)