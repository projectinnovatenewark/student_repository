"""
Modify the example from week 3 lesson 3's game function
"""

# Original Lesson Solution:
from random import randint

def inquireUserGames():
    """ask a user how many times they want to play"""
    timesToPlay = input("How many times would you like to play the 'Guess the Number' game?: ")
    numTimesToPlay = int(timesToPlay)
    userStartedGameString = "You've signed on to play {} games!".format(timesToPlay)
    # Let's return TWO variables to display some cool Python functionality. We can now
    # set two variables equal to the value of calling this function.
    return numTimesToPlay, userStartedGameString

def playTheGame():
    """ask user for a number between 1 and 10, generate a random number between 1 and 10, then see
    if those numbers match. If they do, congratulate the user! If not, tell 'em they guess wrong"""

    # Generate a random number between 1 and 10
    randomNumber = randint(1, 10)
    # Get an input from the user
    promptUserForNumber = input("Guess a number between 1 and 10: ")
    # Convert their input into an integer so you can check for equality between
    # the input and the random number generated
    userNumber = int(promptUserForNumber)

    # Check if the random number and user number equal each other
    if (randomNumber == userNumber):
        print("You guessed correctly! Number", userNumber, "was the correct guess.", "\n")
    else:
        print("Wrong Answer!!! Number", randomNumber, "doesnt equal", userNumber, "\n")

def initializeGame():
    """Lets initialize our game and call the inquireUserGames function."""
    # The first variable will equal the first returned value, and the second variable
    # will equal the second returned value.
    userGameCount, userWelcomeString = inquireUserGames()
    print("\n", userWelcomeString, "\n")

    # userGameCount will equal the user's input from their desired number of games to play.
    # This while loop will continue to run until userGameCount equals zero.
    while userGameCount:
        playTheGame()
        # Every time we run the playTheGame function we want to decrement the userGameCount
        # by one until it hits zero, at which point the while loop will stop running.
        userGameCount -= 1

# Lets call the initializeGame function to get things going!
initializeGame()

# Make sure to comment out the above code before writing your solution.

# This example is from a previous lesson. We want it to ask a user how many times they want
# to play the game, play the game that many times, and tell them when they guess correctly
# along the way. One thing though- the example from the lessons doesn't account for if a user
# inputs something thats NaN (not a number). Implement a try-except-finally to address if the user
# gets a ValueError from entering a non-number. This should probably happen in the inquireUserGames
# function as well as the playTheGame function to ensure that any time a user input is made,
# your function can account for non-number entries.

from random import randint

def inquireUserGames():
    """ask a user how many times they want to play"""

def playTheGame():
    """ask user for a number between 1 and 10, generate a random number between 1 and 10, then see
    if those numbers match. If they do, congratulate the user! If not, tell 'em they guess wrong"""

def initializeGame():
    """Lets initialize our game and call the inquireUserGames function."""

# Lets call the initializeGame function to get things going!
initializeGame()
