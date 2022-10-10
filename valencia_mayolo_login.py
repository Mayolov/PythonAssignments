# Mayolo Valencia
# 10/20/2021
# User has 3 inputs their first name, last name, and 7 digit code
# the method pulls the first 2 characters of the users name
# and then gets the last 3 digits of the users 7 digit code,
# combines them into one string and prints it to the user

def get_login_name(first, last, pin):
    """ The inserted parameters pull string from each
        parameter and gets specific characters out
        to join together into a string."""
    login_name = first[:2:] + last[:2:] + pin[-3:]

    login_name = login_name.lower()
    
    return login_name

def main():
    """ Stores the user inputs into variables the prints
        the function when the parameters are filled with
        the input variables. """
    firstname = input("Please enter your first name: ")
    lastname = input("Please enter your last name: ")
    id_num = input("Please enter a 7 digit id: ")
    
    print('Your login is', get_login_name(firstname, lastname, id_num))
    
# call main to run the program
main()