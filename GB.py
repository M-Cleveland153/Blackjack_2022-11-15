playing = True
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
suits = ('Diamonds','Clubs','Hearts','Spades')

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
            hit(deck, hand)
        else:
            print('please try again')
            continue
        break

def show_some(p_hand, d_hand):
    print("Dealer has: ",'<1st CARD HIDDEN>',d_hand.cards[1], sep = '\n')
    print("\n")
    print("you have:  ",*p_hand.cards,sep='\n')
    print("\n")

def show_all(p_hand, d_hand):
    print("Dealer has:",*d_hand.cards, sep = '\n')
    print('Dealer hand =   ',d_hand.value)
    print("\n")
    print("you have:  ",*p_hand.cards,sep='\n')
    print("your hand =   ",p_hand.value)
    print("\n")

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
