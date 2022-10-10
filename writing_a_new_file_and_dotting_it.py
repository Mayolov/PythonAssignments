import turtle

def makefile(file):
    outfile = open(file, 'w')
    lineadder = True
    
    while lineadder:
        
        addins = input("add to the file: ")
        if addins == 'done':
            lineadder = False
            break
    
        outfile.write(addins + '\n')
    outfile.close()
        


def readfile(file, turt):
    with open(file) as points:
        line = points.readline()

        while line:
            char = line.split()
            if char[0] == 'UP':
                turt.up()
            elif char[0] == 'DOWN':
                turt.down()
            else:
                x,y = int(char[0]),int(char[1])
                turt.goto(x,y)
            line = points.readline()
def main():
  

    quickfile = "mystery.txt"

    makefile(quickfile)
    
    alex = turtle.Turtle()
    win = turtle.Screen()
    
    readfile(quickfile, alex)


    win.exitonclick()
main()
