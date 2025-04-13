import os
text= " today is wonderful day to explore the file handeling in python"
print(os.getcwd()) # get current working directory
os.chdir('C://Users//Chandrasekhar//OneDrive//Desktop//Python-scripting//Filehandeling')# to change the directory
fp=open("write_demo_file.txt",'w')
fp.write(text) # write the content in the file
print("we have coompleted the writing the file")
fp.close() # close the file
# # write the content in the file using with statement
with open('write_demo_file.txt','r') as file:
    print(file.read())
fp.close()
print("***********************Appening the file***********************")
# append the content in the file using with statement
with open('write_demo_file.txt','a') as file:
    file.write("\n this is the appending content in the file")
with open('write_demo_file.txt','r') as file:
    print(file.read()) # read the content of the file after appending
fp.close()