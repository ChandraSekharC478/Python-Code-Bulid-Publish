import os
print(  os.getcwd()) # get current working directory
os.chdir('C://Users//Chandrasekhar//OneDrive//Desktop//Python-scripting//Filehandeling')# to change the directory
print("The current working directory is :",os.getcwd()) # get current working directory
fp=open("sales.txt",'w') # write mode of the file
fp.write("this is an first line we are inserting in the file")
fp.close() # close the file