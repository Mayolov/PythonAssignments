# Mayolo Valencia
# 9/7/21
# This program allows the user to input 5 items and
# finds the subtotal,tax, and total

# constant tax rate
TAX_RATE = 0.07

# prompts the user to input the amount of items they are purchasing
num_items = int(input("How many items are you purchasing? "))

# intializes subtotal
subtotal = 0

# for loop to lessen the amount of lines needed to input item prices
for i in range(num_items):
    item = float(input("enter price for items:" ))
    # += to add subtotal to item
    subtotal += item
    
# Gets the amount of tax to be charged
tax = subtotal * TAX_RATE

# Adds the subtotal and tax
total_sales = subtotal + tax

# Prints the subtotal and formats to 2 decimal spaces max
print("Subtotal: $", format(subtotal,'.2f'), sep="")


# Prints the amount of tax due
print("Tax: $", format(tax,'.2f'), sep="")


# Prints total
print("Total: $", format(total_sales,'.2f'), sep="")