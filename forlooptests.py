
import random

for i in ['January','Febuary','March','April','May','June','July',
          'August','September','October','November','December']:
    print(i, "is a month of the year")

while True:
    try:
        roll_num = input('How many random numbers would you like to generate? ')
        roll_num = int(roll_num)
        break
    except:
        print("\nNumbers only please\n")
        continue
for count in range(roll_num):
    
    print(random.randint(0,99))
    
