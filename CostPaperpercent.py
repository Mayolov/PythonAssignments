# Mayolo Valencia
# 9/7/2021
# This program allows the user to input the number of
# paper packages they need and calculates the cost and tax

# setting an integer value to the variable, CAPS because its constant
COST_PAPER = 2.5

# prompts user to input an integer of # of packages
paper_packages = int(input("How many packages of paper? "))

# prompts user to input the tax rate
tax_rate = float(input("Add tax value: "))

# calculates the subtotal
subtotal = COST_PAPER * paper_packages

# tax rate for paper packages
tax = subtotal * tax_rate / 100 

# Calculates total cost with tax
total_cost = subtotal + tax

# prints total cost to user and formats to nearest 2 decimals
print("Total $", format(total_cost,'.2f'),".", sep="")