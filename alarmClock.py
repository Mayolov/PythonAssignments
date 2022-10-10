# Mayolo Valencia
# 9/9/2021
# Lets the user know what time itll be after inputing their start time
# and their wait time

# Asks user to input current time
current_time = int(input("What is the current time (0-24 hours): "))

# Asks user to input wait time
wait_time = int(input("How many hours are you waiting for? "))

# Calculates the both inputs for end time
total_time = current_time + wait_time

# Gets the final time by finding the remainder
final_time = total_time % 24

# Prints final time
print(final_time)
