class Player:
    def __init__(self, money, name):
        self.money_ = money
        self.name_ = name
    
    def Bet(self, amount):
        self.money = self.money - amount

    def WinningMoney(self, bets):
        self.money += bets