import csv
path="inventory.csv"

def load_csv(path):
    
    #Loads inventory from a CSV file.

    #Returns:
    #list of products
    inventory = []
    errors = 0

    try:
        with open(path, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)

            header = next(reader)
            if header != ["name", "price", "quantity"]:
                raise ValueError("Invalid header")

            for row in reader:
                if len(row) != 3:
                    errors += 1
                    continue

                try:
                    name = row[0]
                    price = float(row[1])
                    quantity = int(row[2])

                    if price < 0 or quantity < 0:
                        raise ValueError

                    inventory.append({
                        "name": name,
                        "price": price,
                        "quantity": quantity
                    })

                except:
                    errors += 1

        print(f"{errors} invalid rows skipped")
        return inventory

    except FileNotFoundError:
        print("File not found.")
    except UnicodeDecodeError:
        print("Encoding error.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return []