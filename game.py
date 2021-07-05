import deck
from player import Player

def Game():
    dealer = Player(1000000, 'Dealer')
    player = Player(10000, 'You')
    Decks = deck.Deck()
    Stop = False
    amount = input('Your bet: ')

    playersCards = []
    dealersCards = []
    
    for i in range (0, 2):
        playersCards.append(Decks.Draw())
        dealersCards.append(Decks.Draw())

    while (not Stop):
        decision = input('Type hit to draw or stop to stop\n').lower()
        if decision == 'hit':
            print('TBA')
        elif decision == 'stop':
            Stop = True
        else:
            print("Unknown command\nType 'y' or 'n'\n")
            continue