# Mayolo Valencia
# 10/7/2021
# the set values are degrees that are point on the globe
# this program calculates the distance between those 2 points
# and print in both kilometers and miles

# bringing in the math module and only bringing out
# sin, acos, cos, radians so 'math.' doesnt have to be used
from math import sin, acos, cos, radians

# function to convert kilometers to miles and converts it to int
def km_to_miles(kliks):
    miles = kliks * .621371
    
    return miles

# gets the center angle and multiplies it with the radius of
# earth to get the distance in kilometers
def great_circle_dist(theta_1, lambda_1, theta_2, lambda_2):
    EARTH_RADIUS = 6371
    
    cent_angle = acos(sin(radians(theta_1)) * sin(radians(theta_2)) \
                           + cos(radians(theta_1)) * cos(radians(theta_2)) \
                           * cos(abs(radians(lambda_1) - radians(lambda_2))))
    distance = EARTH_RADIUS * cent_angle
    
    return distance

# prints the cities and the lat and long of the cities
# then prints the distance between sj to chicago
# then chicago to DC
def main(): 
    # given fixed values for multiple points that are cities
    SJ_LAT = 37.33
    SJ_LONG = -121.9
    CHI_LAT = 41.83
    CHI_LONG = -87.68
    DC_LAT = 38.90
    DC_LONG = -77.02

    # storing the distances in integer values
    dist_sj_chi = great_circle_dist(SJ_LAT, SJ_LONG, CHI_LAT, CHI_LONG)
    dist_chi_dc = great_circle_dist(CHI_LAT, CHI_LONG, DC_LAT, DC_LONG)
    
    # this shows the cities, latitudes, and longitudes in a list form
    print( "City \t \tLatitude Longitude")
    print("\nSan Jose \t ", SJ_LAT, "\u00b0", "\t ", SJ_LONG, "\u00b0",\
          sep='')
    print("\nChicago \t ", CHI_LAT, "\u00b0", "\t ", CHI_LONG, "\u00b0",\
          sep='')
    print("\nWashington, D.C. ", DC_LAT, "\u00b0", "\t ", DC_LONG, "\u00b0",\
          sep='')
    
    # prints the distances between cities in int values
    print("\n\nThe distance from San Jose to Chicago is", \
          int(dist_sj_chi), "kilometers and", \
          int(km_to_miles(dist_sj_chi)), "miles.")

    print("The distance from Chicago to Washington, D.C. is", \
          int(dist_chi_dc), "kilometers and", \
          int(km_to_miles(dist_chi_dc)), "miles.")
    
main()
    
    