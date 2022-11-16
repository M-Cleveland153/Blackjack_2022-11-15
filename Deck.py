import GB
import Card
import random

class Deck:
    def __init__(self):
        self.deck = []
        for suit in GB.suits:
            for rank in GB.ranks:
                self.deck.append(Card.Card(rank, suit))

    def __str__(self):
        print('this deck has:', *self.deck, sep = '\n')

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card
