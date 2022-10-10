# Mayolo Valencia
# 9/9/2021
# Asks user to input day and how long their stay is
# the program calculates what day the final day would be
# in numbers (0-6)

# Asks for start day 0-6
start_day = int(input("What day is it (0-6)? "))

# ask for number of days their stay is
length_of_stay = int(input("How long is your stay? "))

# adds both inputs together
end_number = start_day + length_of_stay

# Finds the remainder
last_day = end_number % 6

# output
print('Your last day is', last_day)