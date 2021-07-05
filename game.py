import deck

def CardCheck(cards):
    sum = 0
    

    return sum
    
def Game(player, dealer):
    Decks = deck.Deck()
    Stop = False
    print(player.money_)
    amount = int(input('Your bet: '))
    player.Bet(amount)
    playersCards = []
    dealersCards = []
    
    for i in range (0, 2):
        playersCards.append(Decks.Draw())
        dealersCards.append(Decks.Draw())

    while (not Stop):
        decision = input('Type hit to draw or stop to stop\n').lower()
        if decision == 'hit':
            playersCards.append(Decks.Draw())
            print(playersCards)
        elif decision == 'stop':
            Stop = True
        else:
            print("Unknown command\nType 'y' or 'n'\n")
            continue
    return player.money_