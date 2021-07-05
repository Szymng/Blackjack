class Player:
    def __init__(self, money, name):
        self.money_ = money
        self.name_ = name
    
    def Bet(self, amount):
        self.money_ = self.money_ - amount

    def WinningMoney(self, bets):
        self.money_ += bets