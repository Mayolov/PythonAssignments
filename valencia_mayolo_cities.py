# Mayolo Valencia
# 11/24/2021
# opens a given file with a long list of cities, countries,
# and populations. It gets opened and read, then split into
# keys (cities) and values(countries and populations) and placed
# into a global dictionary. It then prints the amount of cities
# in the list and the average population. It then prompts the
# user to type in a city of their choosing they dont type
# anything the loop quits, if they type a name not in
# the dictionary it politely says its not in there
# and then continues the loop. If it is in the
# dictionary it then prints the name,country
# and population of the city they chose

def create_dictionary():
    """ Reads a given file and puts its information into
        a dictonary """
    # Can be changed later but is fixed to this file name
    FILE = "cities.txt"
    
    # opens the file and references it  to a variable
    with open(FILE) as city_handle:
        
        # opens a empty dictionary
        city_dict = {}
        
        # goes through each line in the file
        for line in city_handle:
            
            # strips the line and splits it by the commas
            # and adds it into a list 
            city_entries = line.strip().split(',')
            
            # This adds a key and both the values into the empty dictionary
            city_dict[city_entries[0]] = city_entries[1:]
            
    return city_dict
        
    
# capitalizes the users input
def capitalize_city(city_name):
    
    # Uses title() to capitalize it properly 
    return city_name.title()

def main():
    
    # gets the dictoinary from the functions and assigns
    # it to a variabe
    city_dict = create_dictionary()
    
    num_cities = len(city_dict)
    # prints the number of cities
    print("Number of cities:", num_cities)
    
    # initiates a variable
    population_sum = 0
    
    # goes through every key in the dictionary 
    for city in city_dict:
        
        # gets index 1 of the keys and adds it to
        # the previous to get the sum
         population_sum += int(city_dict.get(city)[1])
        
    # get the average population
    average = population_sum / num_cities
    
    # prints average population
    print("Average population: {:,.0f} \n".format(average))
    
    # setting a variable to True so it can be changed later
    user_prompt = True
    
    # While loop to keep asking the user type in a city until they only
    # press enter
    while user_prompt:
        
        city_name = input("Enter a city, or just ENTER to quit: ")
        
        # if nothing is input, make the variable false
        # and quits
        if city_name == "":
            
            user_prompt = False
           
        # capitalizes the city thats input
        else:
            # sets a variable for the new capitalized city name
            capital_city = capitalize_city(city_name)
            
            # if the city is in the dictionary print the values
            if capital_city in city_dict:
                
                population_country = city_dict.get(capital_city)
                
                print(capital_city , "is in" , population_country[0], \
                    "and has a population of {:,.0f}." \
                      .format(int(population_country[1])))
                
            # If the city isnt in the dictionary print this
            else:
                
                print(capital_city, "is not in the list, sorry.")

# run main to execute program
main()