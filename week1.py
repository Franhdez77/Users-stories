valor = True

# Ask the name of product

while valor == True:
    name = str(input("name of product: "))
    if name.replace(" ","").isalpha():
        break
    else:
        print("Invalid Product. Try again")

# Ask the price of product

while valor == True:
    
    try:
        price= float(input("Price of product: "))
        if price<=0:
            raise ValueError("Invalid price. Enter a number greater than 0")
        else:
            break
    except ValueError:
        print("Invalid price.")


# Ask the quantity of product

while valor == True:
    try:
        quantity= int(input("quantity of product: "))  
        if quantity<=0:
            raise ValueError("Invalid quantity. Enter a number greater than 0")
        else:
            break
    except ValueError:
        print ("Invalid quantity. Enter a number greater than 0")

# Calculate the final price of the purchase

total_cost= price*quantity

# Print the bill 

print("Product: ",name)
print("Price: ",price)
print ("Quantity: ",quantity)
print("the final price is ",total_cost)

# The program simulates a inventary, asking the name, price and quantity of a product, 
# then, we calculate the total price multiplying the price with the quantity and finally shows the final price 
