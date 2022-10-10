#prints Hello World! in all uppercase
spam = 'Hello World!'
spam = spam.upper()
print(spam)

#prints Hello World in all lowercase
spam = spam.lower()
print(spam)

# if else statement and whatever is inputed turns to lowercase so the
# program can read it and respond one way or another
print("How are you?")
feeling = input()
if feeling.lower() == 'great' :
    print('I feel great too!')
else:
    print("I hope the rest of your days is good!")

# prints true or false statements

# this implies that Hello World is for certain lowercase or uppercase
# both come out false here because its both uppercase and lowercase
print(spam.islower())
print(spam.isupper())

# this shows that it is for certain upper and lowercase
print('HELLO'.isupper())
print('hello'.islower())

# both of these are false because numbers are not upper or lowercase
print('12345'.isupper())
print('12345'.islower())
