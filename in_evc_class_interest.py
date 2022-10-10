# prompts user for loan amount, yearly
# interest rate as a decimal and the number of years
# calculate and display the interest

def get_interest(principal, annual_intrst, years):
    interest = principal * (annual_intrst / 100) * years
    return interest


# prompts user for inputs
def main():
    principal = float(input('What is the amount of the loan? '))
    annual_intrst = \
        float(input('What is the annual interest rate as a percent? '))
    years = float(input('How many years will this loan be for? '))

    interest = get_interest(principal, annual_intrst, years)
    
    print("The simple interest will be $", format(interest,'.2f'),'.',sep='')
    
main()