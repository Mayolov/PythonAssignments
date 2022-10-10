# Mayolo Valencia
# 12/2/2021
# user puts in the values for each of the the lenses
# they then get put into objects and get the f-stop
# return the objects as strings and checks if both
# objects are equal or not


# How can I call the __str__ function. Ive searched a few
# videos and cant seem to find a way to have it be formated properly



# class that holds all the methods
class Lens:
    
    # initializes variables to be used in the class
    def __init__(self, focal_length, aperature):
        
        MIN_VALUE = 1.0
        
        self.focal_length = focal_length
        self.aperature = aperature
        
        if self.focal_length <= 0:
            
            self.focal_length = MIN_VALUE
            
        if self.aperature <= 0:
            
            self.aperature = MIN_VALUE

        
    # need help trying to use this and if im doing it correctly
    def calc_f_stop(self):

        f_stop = self.focal_length / self.aperature
    
        return f_stop

    # returns the parameters of self as strings
    def __str__(self):
        
        return f'{self.focal_length:.1f} {self.aperature:.1f} {self.calc_f_stop:.1f}'
    
    # checks to see if both objects are equal
    def __eq__(self, other):
        
        return self.focal_length == other.focal_length and \
               self.aperature == other.aperature

def main():
    
    # asks for the parameters of object 1
    focal_length_1  = float(input("Enter focal length of first lens in mm: "))
    aperature_1 = float(input("Enter aperture of first lens in mm: "))
    
    # asks for parameters of object 2 
    focal_length_2 = float(input("Enter focal length of second lens in mm: "))
    aperature_2 = float(input("Enter aperture of second lens in mm: "))
    
    # makes an object 1
    lens1 = Lens(focal_length_1, aperature_1)
    
    # makes an object 2  
    lens2 = Lens(focal_length_2, aperature_2)

    # prints the first lens object beforehand
    print("First lens: Focal length: {} mm; Aperature: {} mm; f-stop {} mm".\
              format(lens1.focal_length, lens1.aperature, Lens.calc_f_stop(lens1)))
    
    # calls the __eq__ method to see if they are equal or not
    if Lens.__eq__(lens1, lens2) == True:

        print("The second lens is the same as the first one.")
            
    else:

        print("second lens: Focal length: {} mm; Aperature: {} mm; f-stop {} mm".\
            format(lens2.focal_length, lens2.aperature, Lens.calc_f_stop(lens2)))

main()
