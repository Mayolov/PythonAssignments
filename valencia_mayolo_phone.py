# Mayolo Valencia
# 10/13/2021
# two phone services provide different rates depending
# on the amount of units being used. This shows the price
# of both and lets you know which is cheaper depending on
# the amount of units being used. 

# Constants for plan 1
BASE_PLAN_1 = 9.38
COVERED_PLAN_1 = 65
OVER_LIMIT_COST_1 = .045

# Constants for plan 2
BASE_PLAN_2 = 8.57
COVERED_PLAN_2 = 50
OVER_LIMIT_COST_2 = .052

def get_units():
    """ Gets the user input for units used"""
    units = int(input("Enter number of units used: "))
    return units

def calculate_cost(units, base_cost, base_units, over_limit_cost):
    """ Gets total price for the amount of units being used"""
    if units < base_units:
        price = base_cost
    else:
        price = ((units - base_units) * over_limit_cost) + base_cost
    return price

def main():
    """user input of amount of units and prints prices and which is cheaper"""
    
    # stores the units here
    units = get_units()
    
    # stores the calculated values here
    plan_1_total = calculate_cost( units, BASE_PLAN_1, COVERED_PLAN_1, \
                                    OVER_LIMIT_COST_1)
    plan_2_total = calculate_cost( units, BASE_PLAN_2, COVERED_PLAN_2, \
                                    OVER_LIMIT_COST_2)
    
    # If there are any negative units this is shown instead
    if  units < 0:
        print("You cannot have negative units.")
        
    # prints cost of each plan
    else:
        print("Cost for plan 1: $", format(plan_1_total, '.2f'), sep='')
        print("Cost for plan 2: $", format(plan_2_total, '.2f'), sep='')
        
        # nested if and else statement
        # if service 1 is cheaper it prints. Else the second must be cheaper
        if plan_1_total < plan_2_total:
            print("First plan is cheaper.")
        else:
            print("Second plan is cheaper")

main()