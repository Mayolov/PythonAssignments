
def user_answers(testfile, answers):
    """ this function puts the user input into a new file then
        reads each line from an existing file and compares each
        line to the users input if its not the same it writes 'X'
        into the new file also return the amount of 'X's 
    """
    count = 0
    for line in answers:
        line = line.strip()
        user_answers = input("Please put your answers here: ")
        user_answers = user_answers.upper()
        
        if user_answers == line:
            testfile.write(user_answers + '\n')
            count += 1
        else:
            testfile.write('X\n')
            
    if count >= 15:
        print("You passed!")
    else:
        print("Sorry, you failed")
    
    incorrect = 20 - count
    return incorrect

def incorrect_lines(userfile):
    """ splits the users answers into a list and reads
        the list to give the questions, lines, that they
        got incorrect then puts commas inbetween
    """
    incorrect_list = []
    # splits user file into list
    for line in userfile:
        line = line.strip().split()
        incorrect_list.append(line)

    wrong_answers = []
    # gets the position of the X's and puts them in a list
    for i in range(len(incorrect_list)):
        if incorrect_list[i] == ['X']:
            wrong_answers.append(str(i + 1))
            
    if wrong_answers == []:
        print("Congrats all are correct!")
    else:
        wrong_answers = ", ".join(wrong_answers)
        print("Questions", wrong_answers, "are incorrect")
    
    
def main():
    """ opens files to be able to write in them and read them
        then prints everything properly
    """
    with open("license_answers.txt") as answers:
        with open("user_answers.txt", 'w') as testfile:
            print("You got", user_answers(testfile, answers) \
                  , "answer(s) incorrect")
        with open("user_answers.txt") as testfile:
            incorrect_lines(testfile)

# call main to run program
main()