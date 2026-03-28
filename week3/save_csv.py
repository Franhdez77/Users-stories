import csv

path="inventory.csv"

def save_csv(inventory, path, include_header=True):

    #Saves inventory to a CSV file.
    if not inventory:
        print("Inventory is empty. Cannot save.")
        return

    try:
        with open(path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            if include_header:
                writer.writerow(["name", "price", "quantity"])

            for i in inventory:
                writer.writerow([i["name"], i["price"], i["quantity"]])

        print(f"Inventory saved at: {path}")

    except Exception as e:
        print(f"Error saving file: {e}")