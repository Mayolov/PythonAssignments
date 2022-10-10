# Mayolo Valencia
# 9/21/2021
# User inputs how many markers they are buying
# then the program puts the amount into packs
# and the others into a seperate markers category
# prints subtotal, tax, shipping, then total value

# intializing constants
TAX = .065
SHIPPING =.05
PACK = 3.50
MARK = .80
MARKERS_PER_PACK = 5

# user input
markers = int(input('How many markers are you buying? '))

# seperating markers
packages = markers // MARKERS_PER_PACK
sep_markers = markers % MARKERS_PER_PACK

# gets the price of the packages and pens
priced_pack = packages * PACK
priced_mark = sep_markers * MARK

# gets the subtotal
subtotal = priced_pack + priced_mark

# gets the tax and shipping cost alone
priced_tax = subtotal * TAX
priced_shipping = subtotal * SHIPPING

# adds all together to get total
total_cost = subtotal + priced_tax + priced_shipping

# print statements of the order
print('Number of packages:', packages)
print('Number of seperte markers:', sep_markers)
print('Subtotal:      $', format(subtotal, '.2f'), sep='')
print('Tax:           $', format(priced_tax, '.2f'), sep='')
print('Shipping cost: $', format(priced_shipping, '.2f'), sep='')
print('Total:         $', format(total_cost, '.2f'), sep='')

#i=1
#count=0
#n=10

#while i<=n:

    #print("The double number is "+str(i))

    #i=i*2

    #count = count +1

    #print("the count is "+str(count))
