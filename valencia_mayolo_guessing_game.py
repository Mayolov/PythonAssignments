# Mayolo Valencia
# 10/13/2021
# Generates a random number and user is supposed
# to guess what it is if they decide to not play
# they type in "0" to stop guessing

# import the random module
import random


def play_guessing_game(myst_num):
    """ runs the yes or no's of the game
        
        when the random number gets called into the function
        this tells the user if the answer is too low, high or correct,
        but if the user decides to not they can input '0'"""
    
    guess_counter = 0
    guess_again = True
    print("Guess my number!")
    
    while guess_again:
        guess = int(input("Enter your guess 1-100, or 0 to stop guessing: "))
        
        if guess == 0:
            print("You didn't guess my number (it was", myst_num, ")")
            guess_again = False
        else:
            guess_counter += 1
            
            if guess > myst_num:
                print("Too high")
            elif guess < myst_num:
                print("Too low")
            else:
                print("Congratulations! You guessed the right number in", \
                                   guess_counter, "guesses!")
                guess_again = False
                
def main():
    """ loops to play the game again over and over

        intitializes 'retry' and starts the loop, makes a random number
        runs the guessing game function and asks if the user wants to keep
        playing if they get the answer right or enters '0' if not it goes
        outside the loop"""
    
    retry = "Y"
    
    while retry is "Y":
        myst_num = random.randrange(1, 101)
        
        play_guessing_game(myst_num)
        
        retry = input("\nDo you want to play again (y/n)? ")
        retry = retry.upper()
        
    print("Goodbye. Thanks for playing.")
# calls the main function to run the program 
main()
