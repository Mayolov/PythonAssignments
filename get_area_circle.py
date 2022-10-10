import math
  
def get_area(radius):
    area = math.pi * radius * radius
    return area


def main():
    radius = float(input("what is the radius? "))
    
    circ_answer = get_area(radius)
    print("Area: ",format(circ_answer,'.3f'))
    
main()