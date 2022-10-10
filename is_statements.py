# checks if string is a-z prints false or true
print('hello'.isalpha())
print('hello123'.isalpha())

# checks if string is Alphanumeric a-z 123 prints true or false
print('hello123'.isalnum())
print('hello'.isalnum())

# this is a bit more confusing but it only allows numbers in the string
print('123'.isdecimal())

#if the string is only spaces
print('   '.isspace())

# If the string is in Title Case meaning lowercase comes after capitol letters
print('This Is Title Case'.istitle())
print('This Is Title Case 123'.istitle())
print('This IS nOt Title case'.istitle())

# Asks for age
while True:
    print('What is your age')
    age = input()
    if age.isdecimal() :
        break
    print('Please enter a number for your age.')
    
while True:
    print('Select a new password (letters and numbers only): ')
    password = input()
    if password is not password.isalnum() :
        continue
    print('password can only have letters and numbers.')

attempt= input('what is your password? ')

if attempt != password:
    print('try again')
else:
    print('good')
    
