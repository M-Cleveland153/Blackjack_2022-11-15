import GB
import Chips
import Deck
import Hand

chips = Chips.Chips()
while chips.total > 0:
    deck = Deck.Deck()
    deck.shuffle()
    player = Hand.Hand()
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    dealer = Hand.Hand()
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())

    GB.take_bet(chips)
    GB.show_some(player,dealer)

    while GB.playing:
        GB.hit_or_stand(deck,player)
        GB.show_some(player,dealer)
        if player.value > 21:
            GB.player_bust(chips)
            break

    if player.value <= 21:
        while dealer.value < 17:
            GB.hit(deck,dealer)

        GB.show_all(player,dealer)

        if dealer.value > 21:
            GB.dealer_bust(chips)

        elif dealer.value > player.value:
            GB.dealer_wins(chips)

        elif dealer.value < player.value:
            GB.player_wins(chips)

        else:
            GB.push()

    if chips.total<=0:
        print("you are out of chips. GAME OVER.")
        break

    print(f'you now have {chips.total} chips.')
    new_game = input("play again? y or n:  ")
    if new_game[0].lower() == 'y':
        GB.playing = True
        continue
    else:
        print('see ya')
        break
