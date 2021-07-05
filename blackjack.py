#main file where the blackjack is playing
from game import Game
from player import Player

gameOn = True
money = 10000
dealer = Player(10000000, 'Dealer')


while(gameOn):
    decision = input("Do you want to play? 'y' or 'n'\n").lower()
    if decision == 'y' or decision == 'yes':
        money = Game(Player(money, 'You'), dealer)
    elif decision == 'n' or decision == 'no':
        gameOn = False
    else:
        print("Unknown command\nType 'y' or 'n'\n")
        continue