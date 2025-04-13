import os
print(os.getcwd()) # get current working directory
os.chdir('C://Users//Chandrasekhar//OneDrive//Desktop//Python-scripting//Filehandeling')# to change the directory
# Product details with correct newlines
Product_List = [
    'Name: Laptop\n',
    'Brand: HP\n',
    'Model: HP Pavilion 15\n',
    'Price: 50000\n',
    'Color: Silver\n',
    'Processor: Intel Core i5\n',
    'RAM: 8GB\n',
    'Storage: 512GB SSD\n',
    'Display: 15.6 inch\n',
    'Battery: 4 cell\n',
    'Graphics: Intel UHD Graphics\n',
    'Weight: 1.75 kg\n',
    'Warranty: 1 year\n',
    'Operating System: Windows 10 Home\n',
    'Ports: USB 3.1, HDMI, Ethernet\n',
    'Audio: HP Audio Boost\n',
    'Keyboard: Full-size island-style keyboard\n',
    'Fingerprint Reader: Yes\n',
    'Backlit Keyboard: Yes\n',
    'Webcam: HP TrueVision HD Camera\n',
    'Bluetooth: Yes\n',
]
with open('Product_List.txt','w') as file:
     file.writelines(Product_List) # write the content in the file
file.close() # close the file
# read the content of the file
with open('Product_List.txt','r') as file:
    print(file.read().strip()) # read the content of the file after appending
file.close()
# create an new file and write the content in the file
# copy the content of the file to new file
# Rename the file as backup
# remove the file
#Paste the content of the file in the new file
