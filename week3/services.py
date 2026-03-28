def add_product(inventory, name, price, quantity):
    #Add a product in the inventory.
    inventory.append({
        "name": name,
        "price": price,
        "quantity": quantity
    })


def show_inventory(inventory):
    #show the inventory
    if not inventory:
        print("Inventory empty.")
        return

    for en,i in enumerate(inventory,start=1):
        print(f"{en}-{i['name']} | {i['price']} | quantity: {i['quantity']}")


def search_product(inventory, name):
    #search for a product.
    #Return the product o none.
    for i in inventory:
        if i["name"].lower() == name.lower():
            return i
    return


def update_product(inventory, name, new_price=None, new_quantity=None):

    #update price or quantity of a product

    product = search_product(inventory, name)
    if product:
        if new_price is not None:
            product["price"] = new_price
        if new_quantity is not None:
            product["quantity"] = new_quantity
        return True
    else:
        return False


def erase_product(inventory, name):
    # erase a product

    product = search_product(inventory, name)
    if product:
        inventory.remove(product)
        return True
    return False