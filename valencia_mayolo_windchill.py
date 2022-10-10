# Mayolo Valencia
# 9/13/2021
# User inputs temperature and velocity to receive windchill for the values

# user inputs values in celcius
temp = float(input('Enter temperature in degrees Celsius: '))

# user inputs values in KMPH
wind_velocity = float(input('Enter wind velocity in kilometers/hour: '))

# calculates winchill
windchill = 13.12 + (0.6215 * temp) - (11.37 * wind_velocity ** 0.16) + \
            (0.3965 * temp * wind_velocity ** 0.16)

# prints windchill
print('The wind chill temperature in degrees ceclius is',
      format(windchill,'.3f'))