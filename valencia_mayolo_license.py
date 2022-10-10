# Mayolo Valencia
# 11/4/2021
# when the program starts running it reads a file
# that already has answers on it. It then compares
# it to a list with correct answers and prints the
# amount of correct questions answered aswell as
# the amount of incorrect answers. Then gives which
# were wrong

# correct answers list to compare the users answers
CORRECT_ANSWERS = ['A', 'C', 'A', 'A', 'D', \
                   'B', 'C', 'A', 'C', 'B', \
                   'A', 'D', 'C', 'A', 'D', \
                   'C', 'B', 'B', 'D', 'A' ]

def user_answers_list(user_file):
    """ This creates a list with the users answers
        from the file
    """
    user_list = []
    for letter in user_file:
        user_list += [letter.strip()]
  
    return user_list
    
def comparison(CORRECT_ANSWERS, user_file):
    """ Compares both files and gets the amount of
        right answers and which were wrong then
        returns those values
    """
    MAX_SCORE = 20
    correct = 0
    incorrect_questions = []
    
    for n in range(20):
        if user_file[n] == CORRECT_ANSWERS[n]:
            correct += 1
        else:
            incorrect_questions += [str(n + 1)]
          
    # Gets the amount of incorrect questions
    incorrect = MAX_SCORE - correct
    # joins the wrong questions with comas to be more
    # presentable
    incorrect_questions = ', '.join(incorrect_questions)
    
    return correct, incorrect, incorrect_questions

def pass_or_fail(correct):
    """ When called tells print if the file
        got a score that passed or failed
    """
    PASS = 15
    
    if correct >= PASS:
        print("You passed!")
        
    else:
        print("Sorry, you failed.")
    
def main():
    """ Opens both files then prints the return values of the
        methods giving the amount thats correct and incorrect
        aswell as the question numbers that were incorrect
    """
    with open("license_comparison.txt") as user_file:
        
        # assigns variables to the comparison method
        correct, incorrect_num, incorrect_questions = \
            comparison(CORRECT_ANSWERS, user_answers_list(user_file))
        
        # calls pass or fail method
        pass_or_fail(correct)
        
        print("You answered", correct, "questions correctly and missed" \
              , incorrect_num, "questions")
        print("These questions were incorrect", incorrect_questions)
            
#calls the main method to run it            
main()