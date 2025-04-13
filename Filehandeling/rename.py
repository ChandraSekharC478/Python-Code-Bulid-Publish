import os
print(os.getcwd()) # get current working directory
os.chdir('C://Users//Chandrasekhar//OneDrive//Desktop//Python-scripting//Filehandeling')# to change the directory
old_file_name="write_demo_file.txt"
new_file_name="write_demo_file_renamed.txt"
os.rename(old_file_name,new_file_name) # rename the file
print("file renamed successfully")

# os.remove(new_file_name) # remove the file
# print("file removed successfully")