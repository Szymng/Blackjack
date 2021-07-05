import deck
import random

Decks = deck.Deck().cards

gameOn = True

while(gameOn):
    decision = input("Do you want to continue? 'y' or 'n'\n").lower()
    if decision == 'y' or decision == 'yes':
        print('TBA')
    elif decision == 'n' or decision == 'no':
        gameOn = False
    else:
        print("Unknown command\nType 'y' or 'n'\n")
        continue