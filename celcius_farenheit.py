# Mayolo Valencia
# 9/13/2021
# Converts whatever celcius the user inputs into farenheit

# asks user to input celcius
celsius = float(input('What celsius would you like to input? '))

# calculates farenheit
farenheit = (celsius * 9/5) + 32

# searches for degree symbol by looking for the number of the character
degree = chr(176)

# prints the farenheit with "F" and the degree symbol 'F°'
print('\n', farenheit, ' ', degree, 'F', sep='')

if farenheit < 50:
    print('\nbrrr, you should wear a coat!')
    
elif farenheit > 85:
    print('\n its really hot! Drink water!!')

else:
    print('\nits a nice day out')