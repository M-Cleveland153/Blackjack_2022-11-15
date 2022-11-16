import random
import GameFiles.GameClasses
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
suits = ('Diamonds','Clubs','Hearts','Spades')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

playing = True

class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank,suit))

    def __str__(self):
        print('this deck has:', *self.deck, sep = '\n')

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# class Chips:
#     def __init__(self):
#         self.total = 100 #default
#         self.bet = 0

#     def win_bet(self):
#         self.total += self.bet

#     def lose_bet(self):
#         self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('what is your bet?  '))
        except:
            print("please enter an integer")

        else:
            if chips.bet > chips.total:
                print(f"sorry, you only have {chips.total} chips.")
                continue
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_aces()

def hit_or_stand(deck, hand):
    global playing
    while True:
        x = input('hit or stand?   ')
        if x[0].lower() == 's':
            playing = False
        elif x[0].lower() == 'h':
            hit(deck,hand)
        else:
            print('please try again')
            continue
        break

def show_some(p_hand, d_hand):
    print("Dealer has  :",'<1st CARD HIDDEN>',d_hand.cards[1], sep = '\n')
    print("you have:  ",*p_hand.cards,sep='\n')

def show_all(p_hand, d_hand):
    print("Dealer has  :",*d_hand.cards, sep = '\n')
    print('Dealer hand =   ',d_hand.value)
    print("you have:  ",*p_hand.cards,sep='\n')
    print("your hand =   ",p_hand.value)

def player_bust(chips):
    print("you bust")
    chips.lose_bet()

def dealer_bust(chips):
    print("dealer bust")
    chips.win_bet()

def player_wins(chips):
    print('you win')
    chips.win_bet()

def dealer_wins(chips):
    print('dealer wins')
    chips.lose_bet()

def push():
    print('PUSH')


chips = GameFiles.GameClasses.Chips()
while chips.total>0:
    deck = Deck()
    deck.shuffle()
    player = Hand()
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    dealer = Hand()
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())

    take_bet(chips)
    show_some(player,dealer)

    while playing:
        hit_or_stand(deck,player)
        show_some(player,dealer)
        if player.value > 21:
            player_bust(chips)
            break

    if player.value <=21:
        while dealer.value < 17:
            hit(deck,dealer)

        show_all(player,dealer)

        if dealer.value > 21:
            dealer_bust(chips)

        elif dealer.value > player.value:
            dealer_wins(chips)

        elif dealer.value < player.value:
            player_wins(chips)

        else:
            push()

    if chips.total<=0:
        print("you are out of chips. GAME OVER.")
        break

    print(f'you now have {chips.total} chips.')
    new_game = input("play again? y or n:  ")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('see ya')
        break
