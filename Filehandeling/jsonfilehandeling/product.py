import os 
import shutil
import datetime
import json

# to get the Current working Directory and change the directory 
print(os.getcwd()) # to get the current working directory
os.chdir("C://Users//Chandrasekhar//OneDrive//Desktop//Python-scripting//Filehandeling//jsonfilehandeling")
# Read some Products from json file
# Allow to add the new Products into my panel
# Write updated data back into original file
# create backup from the original file

# method for the backup


# Methof for Writing the products into file


# Read the Produts from file

# method for the adding new Product 
def add_new_product(products):
    print("/n add new Product:")
    try:
        product_id=int(input("Enter the product id(001) :"))
        prouct_name=input("Name of the Product:")
        product_price=float(input("Please give the Product_price:"))
        product_in_stock=int(input("Please give the stock you have for this Product:"))
        new_product={
            product_id:product_id,
            prouct_name:prouct_name,
            product_price:product_price,
            product_in_stock:product_in_stock
        }
        products.append(new_product)
        print("The New Product Got Added to inventory🚀🚀🚀🚀🚀🚀🚀")
    except Exception as ex:
        print(ex)

# method for Displaying all products
def display_products(products):
    if not products:
        print("No products have been present ")