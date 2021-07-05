import deck
import random
import player

Decks = deck.Deck().cards

dealer = player.Player(1000000, 'Dealer')
player = player.Player(10000, 'You')
