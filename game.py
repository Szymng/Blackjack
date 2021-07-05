#single game of blackjack
import deck

def CardSum(cards):
    sum = 0
    aceNumber = 0
    for card in cards:
        if card == 'Ace': #Aces have 1 value and 11, so they will be added after summing up other cards
            aceNumber += 1
        else:
            if card == '2':
                sum += 2
            elif card == '3':
                sum += 3
            elif card == '4':
                sum += 4
            elif card == '5':
                sum += 5
            elif card == '6':
                sum += 6
            elif card == '7':
                sum += 8
            elif card == '9':
                sum += 9
            else:
                sum += 10
    for ace in range(0, aceNumber): #adding aces to sum
        if sum < 11:
            sum += 11
        else:
            sum += 1
    return sum

def CheckSum(playerSum, dealerSum):
    if abs(21 - playerSum) < abs(21 - dealerSum) and playerSum < 22 and dealerSum < 22:
        return 'win'
    elif playerSum > 21 and dealerSum < 22:
        return 'lose'
    elif abs(21 - playerSum) > abs(21 - dealerSum) and playerSum < 22 and dealerSum < 22:
        return 'lose'
    elif playerSum == dealerSum and playerSum < 22:
        return 'Draw'
    
def Game(player, dealer):
    Decks = deck.Deck()
    Stop = False
    print(player.money_)
    amount = int(input('Your bet: '))
    player.Bet(amount)
    bets = amount*2
    playersCards = []
    dealersCards = []
    playerSum = 0
    dealerSum = 0

    #first hand
    for i in range (0, 2):
        playersCards.append(Decks.Draw())
        dealersCards.append(Decks.Draw())
    
    #print your current hand and its value
    print(playersCards)
    playerSum = CardSum(playersCards)
    dealersCards = CardSum(dealersCards)

    print(playerSum)
    while (not Stop):
        decision = input('Type hit to draw a card or stop to stop\n').lower()
        if decision == 'hit': #draw a card
            playersCards.append(Decks.Draw())
            
            #print your current hand and its value
            print(playersCards)
            playerSum = CardSum(playersCards)
            print(playerSum)
        elif decision == 'stop': #stop drawing
            Stop = True
        else:
            print("Unknown command\nType 'y' or 'n'\n")
            continue
        if playerSum > 21: #check if player needs to draw more cards
            Stop = True
    
    areYouWinning = CheckSum(playerSum, dealerSum) #check win condition
    if areYouWinning.lower() == 'win':
        print('You won!')
        player.WinningMoney(bets)
    elif areYouWinning.lower() == 'draw':
        print("It's a draw")
        player.WinningMoney(bets/2)
    elif areYouWinning.lower() == 'lose':
        print('You lost')
    return player.money_