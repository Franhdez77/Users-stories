# Inventory list
inventory = []

# Function: Add product
def add_product():
    
    #Adds a new product to the inventory.
    
    try:
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        # Validate values
        if price < 0 or quantity < 0:
            print("Price and quantity must be positive.")
            return

        product = {
            "name": name,
            "price": price,
            "quantity": quantity
        }

        inventory.append(product)
        print("Product added successfully.")

    except:
        print("Invalid input. Please enter correct values.")


#Function to show the inventory
def show_inventory():
    
    #Displays all products in the inventory.

    if not inventory:
        print("Inventory is empty.")
        return

    for p in inventory:
        print(f"Product: {p['name']} | Price: {p['price']} | Quantity: {p['quantity']}")


#function to calculate the statistics
def calculate_statistics():
    
    #Calculates total value and total quantity.
    if not inventory:
        print("Inventory is empty.")
        return

    total_value = 0
    total_quantity = 0

    for i in inventory:
        total_value += i["price"] * i["quantity"]
        total_quantity += i["quantity"]

    print(f"Total inventory value: {total_value}")
    print(f"Total products quantity: {total_quantity}")


# Main menu
while True:
    print("\n--- MENU ---")
    print("1. Add product")
    print("2. Show inventory")
    print("3. Calculate statistics")
    print("4. Exit")

    option = input("Choose an option: ")

    # Conditional structure
    if option == "1":
        add_product()

    elif option == "2":
        show_inventory()

    elif option == "3":
        calculate_statistics()

    elif option == "4":
        break

    else:
        print("Invalid option. Try again.")


# This program allows managing an inventory using
# lists, dictionaries, loops, and conditionals.
# It validates input and calculates basic statistics.