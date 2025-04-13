# to read the content in an file 
# find the path of the file in the system'
# open the file in read mode
# Read conent from the file 
#  Read() method reads the entire content of the file and returns it as a string.
#  readline() method reads a single line from the file and returns it as a string.
#  readlines() method reads all the lines from the file and returns them as a list of strings.
#  close the file
import os
print(os.getcwd()) # get current working directory
os.chdir('C://Users//Chandrasekhar//OneDrive//Desktop//Python-scripting//Filehandeling')# to change the directory
with open('sales.txt','r') as fp: # read mode 
    content=fp.read() # Read the entire content of the file
    print(content) # print the content of the file
    fp.close() # close the file
# Read the first line of the file
print("************************ReadingFirstLine*************************")
def read_first_line(file_path):
    with open(file_path,'r') as file:
        first_line=file.readline()
        return first_line.strip()

print(read_first_line('sales.txt')) # print the first line of the file  
print("************************ReadingAllLines*************************")
def read_all_lines(file_path):
    with open(file_path,'r') as file:
        lines=file.readlines()
        print(lines)
print(read_all_lines('sales.txt')) # print all the lines of the file
 # write an program to print first 4 lines of the file
print("************************ReadingFirstFourLines*************************")
def first_four_line(file_path):
    with open(file_path,'r')as file:
        for i in range(4):
            print(file.readline().strip())
first_four_line('sales.txt') # print first four lines of the file
# print first and last line of the file
print("************************ReadingFirstAndLastLine*************************")
def first_and_last_line(file_path):
    with open(file_path,'r') as file:
        firstline=file.readline().strip()
        print("First line:",firstline)
        for i in file:
            pass
        lastline=i
        print("Last line:",lastline)
first_and_last_line('sales.txt') # print first and last line of the files
