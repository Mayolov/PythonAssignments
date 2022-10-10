# Mayolo Valencia
# 10/11/2021
# This program recieves the users input of hours and hourly rate
# from there job and calculates it to print out the users total pay
# for the week

def wages(hours_worked, hourly_rate):
    """ calculates total pay for user input """
    
    if hours_worked <= 40:
        pay = hours_worked * hourly_rate
    else:
        pay = (hourly_rate * 40) + ((hours_worked - 40) \
                                        * (hourly_rate * 1.5))
    return pay
    
def main():
    """ input for hours worked and wage and prints the result """
    
    hrs_worked = float(input \
                       ('Enter the number of hour sworked in the week: '))
    hourly_rate = float(input('Enter the hourly rate: '))
    
    print('Total wages for the week: $',
          format(wages(hrs_worked, hourly_rate), ',.2f'), sep='')

# main function is called to run the methods
main()