class Chips:
    def __init__(self):
        self.total = 100 #defualt

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet