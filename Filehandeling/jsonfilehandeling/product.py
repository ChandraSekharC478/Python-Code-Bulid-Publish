import os 
import shutil
import datetime
import json

# to get the Current working Directory and change the directory 
print(os.getcwd()) # to get the current working directory
os.chdir("C://Users//Chandrasekhar//OneDrive//Desktop//Python-scripting//Filehandeling//jsonfilehandeling")
DATA_FILE = "products.json" # the file name where the data is stored
DATA_BACKUP_FILE = "products_backup.json" # the file name where the backup is stored
DATA_DIR = os.path.dirname(os.path.abspath(__file__)) # to get the directory of the file

# Read some Products from json file
# Allow to add the new Products into my panel
# Write updated data back into original file
# create backup from the original file

# main Method
def main():
    print("Welcome to the Product Inventory Management System")
    products= read_products_from_file() # read the products from the file
    display_products(products) # display the products in the file
    user_choice = input("Do you want to add a new product? (yes/no): ").strip().lower() # ask the user if they want to add a new product
    if user_choice == "yes":
        create_backup() # create a backup of the file
        print("Backup created successfully")
        add_new_product(products) # add the new product to the file
        write_products_to_file(products) # write the products to the file
    else:
        print("No new product added")

# method for the backup
def create_backup():
    # Step 1: Check if the source file (products.json) exists
    if os.path.exists(DATA_FILE):
        # Step 2: Get the current timestamp for creating a unique backup file name
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Step 3: Create the backup file name using the timestamp
        backup_file_name = f"products_backup_{timestamp}.json"
        
        # Step 4: Create the 'backup' folder if it doesn't exist
        backup_folder = os.path.join(DATA_DIR, "backup")
        if not os.path.exists(backup_folder):
            os.makedirs(backup_folder)  # Create the folder if it doesn't exist
        
        # Step 5: Create the full path for the backup file inside the 'backup' folder
        backup_file_path = os.path.join(backup_folder, backup_file_name)
        
        try:
            # Step 6: Copy the original file to the backup location
            shutil.copy(DATA_FILE, backup_file_path)
            # Step 7: Confirm success
            print(f"Backup created successfully: {backup_file_path}")
        except Exception as ex:
            # Step 8: Handle any errors during the backup process
            print(f"Error during backup creation: {ex}")
    else:
        # Step 9: If the source file doesn't exist, notify the user
        print(f"The file {DATA_FILE} does not exist. Backup cannot be created.")
# Method for Writing the products into file
def write_products_to_file(products):
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(products, file, indent=4) # write the content in the file
            print("The Products Got written to the file successfully")
    except Exception as ex:
        print(ex)


# Read the Produts from file
def read_products_from_file():
    if not os.path.exists(DATA_FILE):
        print("The file does not exist")
        return []
    try:
        with open(DATA_FILE, "r") as file:
            products = json.load(file) # read the content of the file
            print("The Products Got read from the file successfully")
            return products
    except Exception as ex:
        print(ex)
        return []

# method for the adding new Product 
def add_new_product(products):
    print("\nAdd New Product:")
    try:
        product_id = int(input("Enter the product ID (e.g., 001): "))
        product_name = input("Name of the Product: ")
        product_price = float(input("Enter the product price: "))
        product_in_stock = int(input("Enter how many units are in stock: "))
        
        new_product = {
            "id": product_id,
            "name": product_name,
            "price": product_price,
            "in_stock": product_in_stock
        }

        products.append(new_product)
        print("✅ The new product was added to the inventory successfully 🚀")
    except Exception as ex:
        print(f"❌ Error while adding product: {ex}")


# method for Displaying all products
def display_products(products):
    if not products:
        print("No products have been present")
    else:
        print("The Products available in the inventory are:")
        for product in products:
            print(f"Product ID: {product['id']}, Name: {product['name']}, Price: {product['price']}, In Stock: {product['in_stock']}")
            print("-----------------------------------------------------------------")
main() # call the main method
