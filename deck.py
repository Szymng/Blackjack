import random
class Deck:
    cards = [
        'Ace',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        'Jack',
        'Queen',
        'King'
    ]
    def Draw(self):
        card = random.choice(list(self.cards))
        return card