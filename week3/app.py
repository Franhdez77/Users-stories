from services import *
from save_csv import *
from load_csv import *
from stats import *

inventory = []

while True:
    print("\n MENU")
    print("1. Add products")
    print("2. Show products")
    print("3. Search product")
    print("4. Update product")
    print("5. Delete product")
    print("6. Statistics")
    print("7. Save CSV")
    print("8. Load CSV")
    print("9. Exit")

    try:
        option = int(input("Select an option: "))

        if option == 1:
            name = input("Name: ")
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))
            add_product(inventory, name, price, quantity)

        elif option == 2:
            show_inventory(inventory)

        elif option == 3:
            name = input("Search: ")
            search = search_product(inventory, name)
            if search:
                print(search)
            else:
                print("Not found")

        elif option == 4:
            name = input("Product: ")
            price = float(input("New price: "))
            quantity = int(input("New quantity: "))

            update_product(
                inventory,
                name,
                price,
                quantity
            )

        elif option == 5:
            name = input("Product to erase: ")
            erase_product(inventory, name)

        elif option == 6:
            stats = calculate_stats(inventory)
            if stats:
                print(stats)
            else:
                print("Inventory is empty.")

        elif option == 7:
            save_csv(inventory, path)

        elif option == 8:
            load_csv(path)

        elif option == 9:
            break

        else:
            print("Invalid option.")

    except Exception as e:
        print(f"Error: {e}")