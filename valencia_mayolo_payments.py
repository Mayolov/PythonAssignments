# Mayolo Valencia
# 9/13/2021
# runs the users input values and calculates the monthly payments
#of the pricipal loan including interest over time

# function that gets the user inputs 
def intpayments(yearly_rate, loan_length_years, principal):
    
    # divides the yearly rate to get the monthly rate (r)
    monthly_rate = (yearly_rate / 12) / 100

    # changes years into months (n)
    loan_length_months = loan_length_years * 12

    # sub formula to make formula easier to read
    subform = (1 + monthly_rate) ** loan_length_months

    # calculation of the payment
    payment = principal * monthly_rate * subform / (subform - 1)

    return payment

# main function that asks for the user inputs
def main():
    # user inputs for principal, interest, and length of loan
    principal = float(input('Enter amount of loan: '))
    yearly_rate = float(input('Enter annual interest rate as a percent: '))
    loan_length_years = float(input('Enter number of years for the loan: '))
    
    # calls the other method and sets it to a variable to be orinted
    payment = intpayments(yearly_rate, loan_length_years, principal)
    
    # prints what your monthly payment is and only allows till the 2nd decimal
    print('Your monthly payment is $', format(payment,'.2f'), sep='')

# calling the main method to show everything
main()