# Mayolo Valencia
# 11/24/2001
# By importing another program to use its functions and
# classes. This program asks the user for 2 times, in
# European time, and in AM/PM seperateeed by a coma.
# We then seperate both of them using split() and
# make both times into objects. When doing so it
# seperates both into hours and minutes to be easily
# used to add and subtract the values later. Then
# it prints what the user put in, the sum, and differnece

import clock

def seperate_times(times):
    """ seperates the users times """
    
    seperated = times.split(",")
    
    return seperated[0], seperated[1]

def main():
    """ User inputs their times and until nothing is
        entered it keeps looping. It will print
        the times they put in, in military time and
        then print the sum and difference of both times
    """
    
    # initializing variable to change later
    prompt_user = True
    
    # while loop
    while prompt_user:
        
        # asks user for to input times and stores the input in a variable
        times = input("Enter military time and AM/PM time " + \
                "separated by a comma \nor just press ENTER to quit: ")
                
        # If nothing is entered quit
        if times == "":
            
            # when false the while loop ends
            prompt_user = False
        
        else:
            
            # gives a variable to reference the return values
            mil_time, civ_time = seperate_times(times)
            
            # makes the previous variables into objects
            # and give them hour and time attributes
            mil_time_obj = clock.from_military(mil_time)
            civ_time_obj = clock.from_am_pm(civ_time)
            
            # returns what the user input but both in military time
            print("You entered", mil_time_obj, "and", civ_time_obj)
            
            # adds mil_time and the civ_time together and prints
            print("The sum of the times is", mil_time_obj.add(civ_time_obj))
            
            # subtracts mil_time and the civ_time together and prints
            print("The difference of the times is", \
                  mil_time_obj.subtract(civ_time_obj))
            
# runs the main function
main()