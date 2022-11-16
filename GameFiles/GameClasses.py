# class Card:
# 	def __init__(self,rank,suit):
# 		self.rank = rank
# 		self.suit = suit

# 	def __str__(self):
# 		return self.rank + ' of ' + self.suit

# class Deck:
# 	def __init__(self):
# 		self.deck = []  # start with empty list
# 		for suit in suits:
# 			for rank in ranks:
# 				self.deck.append(Card(suit,rank))

# 	def __str__(self):
# 		deck_comp = ''
# 		for card in self.deck:
# 			deck_comp += '\n '+car.__str__()
# 		return 'the deck has: ' + deck_comp

# 	def shuffle(self):
# 		random.shuffle(self.deck)

# class Hand:
# 	def __init__(self):
# 		self.cards = []
# 		self.value = 0
# 		self.aces = 0

# 	def add_card(self,card):
#         self.cards.append(card)
#         self.value += values[card.rank]
#         if card.rank == 'Ace':
#             self.aces += 1

#     def adjust_aces(self):
#         while self.value > 21 and self.aces:
#             self.value -= 10
#             self.aces -= 1

class Chips:
    def __init__(self):
        self.total = 100 #default
        self.bet = 0

    def win_bet(self):self.total+=self.bet
    def lose_bet(self):self.total-=self.bet