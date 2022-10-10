#def get_multiples(first_num, last_num):
#    count_multiples = 0
#    
#    for n in range(first_num, last_num + 1):
#        if n % 7 == 0 :
#            count_multiples += 1
#            
#    return count_multiples
#            
#
#def main():
#    multiples = get_multiples(1,1000)
#
#    print("There are", multiples, "of 7 or 5 from 1-1000")   
#
#main()

def age_cost(age):
    
    if age <= 3:
        cost = 0
    elif age<= 14:
        cost = 17
    elif age <= 64:
        cost = 23
    else:
        cost = 19
    return cost
    
    
def main():
    age = int(input("Whats the age: "))
    print(f'The buffet costs ${age_cost(age):.2f}')

main()















#count = 0
#for i in range(0,1000,7):
#    count+=1
#print(count)
