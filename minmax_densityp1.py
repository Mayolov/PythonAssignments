# Mayolo Valencia
# 11/1/2021
# Reads a list and find different ranges within the list
# min, max, median, average. This reads each line in the
# text file and splits it to get the 2nd character which
# is the density for every planet

def pnlist(file):
    """ Opens the file and through the for loop seperates
        the planets and densities into 2 different lists
        and returns a third list as the sorted density list
    """

    planet_list = []
    density_list = []
    for line in file:
        char = line.split()
        planet_list.append(char[0])
        density_list.append(float(char[1]))
            
    return planet_list, density_list, sorted(density_list)
    
def min_max(planet, density):
    """ Finds the index for the min and max numbers then
        inputs and uses it to retrieve the character in
        indexx of the list
        
        Returns 4 values minimum planet its denity then
        maximum planet and its density
    """
    minimum = density.index(min(density))
    maximum = density.index(max(density))
    
    return planet[minimum], min(density), planet[maximum], max(density)

def average(density_list):
    """ again using the list method it adds up all the
        numbers and then divides it by the length of the
        list
    """
    listsum = 0
    for i in density_list:
        
        listsum += i
    avg = listsum / len(density_list)
    
    return avg

def median(sorted_list):
    """ find the median of the list either if its
        odd or even and returns the median"""
    if len(sorted_list) % 2 == 1:
        mid_num = sorted_list[(len(sorted_list) - 1) // 2]
    else:
        mid_num = (sorted_list[(len(sorted_list) // 2)] + \
                   sorted_list[(len(sorted_list) // 2) - 1]) / 2.0 
    return mid_num

def main():
    """ Calls the necessary functions to print the statments
        properly, and assigns objects to variables for easier
        use
    """
    with open("density.txt", 'r') as file_handle:
        
        list_function = pnlist(file_handle)
        min_n_max = min_max(list_function[0],list_function[1])
        
        print(min_n_max[2], "has the largest density in the solar system" \
             , "at" , min_n_max[3] , "grams per cubic centimeter.")
        
        print(min_n_max[0], "on the otherhand is the least dense at" \
             , min_n_max[1], "grams per cubic centimeter.\n")
            
        print("The average density of the solar system, including pluto, is" \
                  ,"{:.2f} grams per cubic centimeter." \
              .format(average(list_function[1])) )
            
        print("The median is {:.2f} grams per cubic centimeter." \
                  .format(median(list_function[2])))
            
# call the main method to run the program
main()