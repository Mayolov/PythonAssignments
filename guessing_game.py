myNumber = 5
numTries = 1
gameOver = False

while gameOver != True:
    guess = int(input("Whats your guess 1-10?"))

    if guess > myNumber:
        print("Too high!")

    elif guess < myNumber:
        print("Too Low")
        
    else:
        print("You got it!")
        print("you got it in", numTries , "try(s)")
        gameOver =True
    numTries +=1
  
