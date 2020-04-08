"""
Create a random card generator
"""
# TODO: You are going to be creatng a random card generator using a combination of things 
# TODO: you've learned to date. First you should import 'randint' from 'random'.
# TODO: This will be used later. Next you should define a function called 'randomCard'
# TODO: and pass it the argument 'deck'. This is where you'll use 'randint' to generate the random card.
# TODO: HINT: You should return the value of the randomCard ;)
from random import randint

cardSuits = ["Hearts", "Diamonds", "Spades", "Clubs"]
cardValues = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

def randomCard(deck):
    randIndex = randint(0, 51)
    randomCard = deck[randIndex]
    return randomCard

# TODO: Next you should define a function 'createDeck'. I suggest you create an empty list to be filled.
# TODO: This list will be filled with a full deck (i.e. 2 of Hearts, 
# TODO: 3 of Hearts... all the way to Ace of Clubs)
# TODO: I think nested for loops might be the way to go to crack this
# TODO: But what do i know :) Also, Return your list!

def createDeck():
    deck = []
    for value in cardValues:
        for suit in cardSuits:
            deck.append(f"{value} of {suit}")
    return deck

# TODO: Lastly, define a function 'main'. Here you'll want to create variable that hold your
# TODO: called 'createDeck' and 'randomCard' functions.
# TODO: Then simply print and the random card in your 'main' function and finally; call 'main'.

def main():
    fullDeck = createDeck()
    randCard = randomCard(fullDeck)
    print(randCard)

main()