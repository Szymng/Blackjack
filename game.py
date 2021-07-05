import deck
import random
from player import Player

def Game():
    dealer = Player(1000000, 'Dealer')
    player = Player(10000, 'You')
    Decks = deck.Deck().cards
    Stop = False
    amount = input('Your bet: ')

    while (not Stop):
        decision = input('Type hit to draw or stop to stop\n').lower()
        if decision == 'hit':
            print('TBA')
        elif decision == 'stop':
            Stop = True
        else:
            print("Unknown command\nType 'y' or 'n'\n")
            continue