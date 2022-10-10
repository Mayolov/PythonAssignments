
def print_triangular_numbers(n):
    # your code here
    counter = 0
    for i in range(n):
        counter+=1 
        answer= (counter*(counter+1))/2
        print(counter, int(answer))
    return answer

print_triangular_numbers(5)

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(25))
print(is_prime(7))
print(is_prime(251))
print(is_prime(20))
