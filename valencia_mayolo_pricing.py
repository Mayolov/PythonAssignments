# Mayolo Valencia
# 10/11/2021
# This program calculates the a total cost before and after
# its discount and also print the amount the products will be
# discounted depending on the quantitity

def get_discount_rate(quantity):
    """ Depending on the quantity of the
        product the discount percentage
        changes """
    
    if quantity < 10:
        discount_rate = 0
    elif quantity < 20:
        discount_rate = .10
    elif quantity < 50:
        discount_rate = .20
    elif quantity < 100:
        discount_rate = .25
    else:
        discount_rate = .30   
    return discount_rate

def main():
    
    """ User input for a float value of the price
        and an integer value for the quantity.
        Then prints the original price, discount
        amount, and total price """
    
    price = float(input('Enter price of product: '))
    quantity = int(input('Enter quantity: '))
    
    # finds the original cost, discount amount, and final cost after discount
    orig_price = price * quantity
    discount = orig_price * get_discount_rate(quantity) 
    total_price = orig_price - discount
    
    print('Total price before discount: $', format(orig_price, ',.2f'), sep='')
    print('Amount of discount: $', format(discount, ',.2f'), sep='')
    print('Total price after discount: $', format(total_price, ',.2f'), sep='')

# call the main function to run methods
main()