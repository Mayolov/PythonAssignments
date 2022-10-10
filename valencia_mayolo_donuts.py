# Mayolo Valencia
# 10/7/2021
# This program asks the user to input the amount of each donut
# they'd like. It then seperate the amount between dozens and single for
# both categories. They multiply themselves to their corresponding value
# then add themselves with its own category to get the subtotal for that
# category. Both categories add together to give us the total and everything
# is then printed individualy

# fixed values for the donut categories
PLAIN_DOZEN = 7.0
PLAIN_SINGLE = .60
FANCY_DOZEN = 9.0
FANCY_SINGLE = .80

# asks for user input
buy_plain = int(input('Enter number of plain donuts you want to buy: '))
buy_fancy = int(input('Enter number of fancy donuts you want to buy: '))

# seperates the donuts per category into dozens or singles
p_doz_amnt = buy_plain // 12
p_sngl_amnt = buy_plain % 12 
f_doz_amnt = buy_fancy // 12
f_sngl_amnt = buy_fancy % 12

# these both get the subtotal for their own respective category
plain_subtotal = (p_doz_amnt * PLAIN_DOZEN) + (p_sngl_amnt * PLAIN_SINGLE)
fancy_subtotal = (f_doz_amnt * FANCY_DOZEN) + (f_sngl_amnt * FANCY_SINGLE)

# this is the total of both categories combined
total_amnt = fancy_subtotal + plain_subtotal

# print plain dozen, single, and cost
print("Plain donuts", "\n ", p_doz_amnt, " dozen and " \
      , p_sngl_amnt, " single ", "\n"," Cost: $", \
      format(plain_subtotal,'.2f'), sep='')

# print fancy dozen, single, and cost
print("Fancy donuts", "\n ", f_doz_amnt, " dozen and " \
      , f_sngl_amnt, " single ", "\n"," Cost: $", \
      format(fancy_subtotal,'.2f'), sep='')

# prints total amount of everything combined
print("Total amount due: $", format(total_amnt,'.2f'), sep='')