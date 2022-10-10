# Mayolo Valencia
# 9/8/2021
# This programs has a set of fixed variables but allows
# the user to input the amount of years giving the amount
# of money the user has gained through compound interest in those
# years

# Principal
P = 10000

# Compounding rate
N = 12

# Interest
R = 8/100

# User input of years
t = int(input("How many years will it be compounded? "))

# Formula to find the total after user inputs # of years
total = P * (1 + (R / N)) ** (N * t)

# Prints final amount after compounding
print("\nFinal amount after ", t, " Years is $", format(total, '.2f'), sep="")