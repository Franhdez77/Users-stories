def calculate_stats(inventory):
    
    #Calculates inventory statistics.
    #Return dict with metrics or none if empty

    if not inventory:
        return None

    subtotal = lambda p: p["price"] * p["quantity"]

    total_units = sum(p["quantity"] for p in inventory)
    total_value = sum(subtotal(p) for p in inventory)

    most_expensive = max(inventory, key=lambda p: p["price"])
    highest_stock = max(inventory, key=lambda p: p["quantity"])

    return {
        "total_units": total_units,
        "total_value": total_value,
        "most_expensive": (most_expensive["name"], most_expensive["price"]),
        "highest_stock": (highest_stock["name"], highest_stock["quantity"])
    }