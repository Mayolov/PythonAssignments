# Mayolo Valencia
# 11/1/2021
# Reads a list and find different ranges within the list
# min, max, median, average. This reads each line in the
# text file and splits it to get the 2nd character which
# is the density for every planet

def planets_lists(file):
    """ Opens the file and through the for loop seperates
        the planets and densities into 2 different lists
    """
    planet_list = []
    density_list = []
    
    # reads through each line of the text file and strips
    # then splits the line and puts the first entry into
    # one list and the second into another
    for line in file:
        planet_density = line.strip().split()
        planet_list.append(planet_density[0])
        density_list.append(float(planet_density[1]))
            
    return planet_list, density_list
    
def min_max(planet, density):
    """ Finds the index for the min and max numbers then
        inputs and uses it to retrieve the character in
        indexx of the list
        
        Returns 4 values minimum planet its density then
        maximum planet and its density
    """
    
    minimum = min(density)
    maximum = max(density)
    
    min_index = density.index(minimum)
    max_index = density.index(maximum)
    
    return planet[min_index], minimum, planet[max_index], maximum

def average(density_list):
    """ again using the list method it adds up all the
        numbers and then divides it by the length of the
        list
    """
    n = len(density_list)
    
    if n == 0:
        avg = 0
        
    else:
        avg = sum(density_list) / n
    
    return avg

def median(density_list):
    """ find the median of the list either if its
        odd or even and returns the median
    """
    
    # sorts the desnities
    density_list = sorted(density_list)
    
    # find the median
    if len(density_list) % 2 == 1:
        mid_num = density_list[(len(density_list) - 1) // 2]
    else:
        mid_num = (density_list[(len(density_list) // 2)] + \
                   density_list[(len(density_list) // 2) - 1]) / 2.0
        
    return mid_num

def main():
    """ Calls the necessary functions to print the statments
        properly, and assigns objects to variables for easier
        use
    """
    with open("density.txt", 'r') as file_handle:
        
        # three_lists is the return of the three lists from the planet_list
        # function [0] is for the planet names, [1] is for the densities, and
        two_lists = planets_lists(file_handle)
        
        # obtain the minimum and maximum using the three_lists
        # and gives the planet name for the density
        min_n_max = min_max(two_lists[0], two_lists[1])

        print(min_n_max[2], "has the largest density in the solar system" \
             , "at" , min_n_max[3] , "grams per cubic centimeter.")
        
        print(min_n_max[0], "on the otherhand is the least dense at" \
             , min_n_max[1], "grams per cubic centimeter.\n")
            
        print("The average density of the solar system, including pluto, is" \
                  , "{:.2f} grams per cubic centimeter." \
              .format(average(two_lists[1])) )
            
        print("The median is {:.2f} grams per cubic centimeter." \
                  .format(median(two_lists[1])))
            
# call the main method to run the program
main()