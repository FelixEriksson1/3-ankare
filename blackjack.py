import random

# create a deck of cards
deck = []
suits = ['hearts', 'diamonds', 'clubs', 'spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
for suit in suits:
    for rank in ranks:
        card = rank + ' of ' + suit
        deck.append(card)

# shuffle the deck
random.shuffle(deck)

# deal two cards to the player and the dealer
player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]

# calculate the player's and dealer's scores
player_score = 0
for card in player_hand:
    rank = card[0]
    if rank == 'J' or rank == 'Q' or rank == 'K':
        player_score += 10
    elif rank == 'A':
        player_score += 11
    else:
        player_score += int(rank)

dealer_score = 0
for card in dealer_hand:
    rank = card[0]
    if rank == 'J' or rank == 'Q' or rank == 'K':
        dealer_score += 10
    elif rank == 'A':
        dealer_score += 11
    else:
        dealer_score += int(rank)

# check for blackjack
if player_score == 21:
    print("Player has blackjack and wins!")
elif dealer_score == 21:
    print("Dealer has blackjack and wins!")
else:
    # player's turn
    while True:
        choice = input("Do you want to hit or stand? ")
        if choice == 'hit':
            player_hand.append(deck.pop())
            player_score = 0
            for card in player_hand:
                rank = card[0]
                if rank == 'J' or rank == 'Q' or rank == 'K':
                    player_score += 10
                elif rank == 'A':
                    player_score += 11
                else:
                    player_score += int(rank)
            print("Player's hand:", player_hand)
            print("Player's score:", player_score)
            if player_score > 21:
                print("Player busts and loses.")
                break
        elif choice == 'stand':
            break
        else:
            print("Invalid choice. Please enter hit or stand.")

    # dealer's turn
    if player_score <= 21:
        while dealer_score < 17:
            dealer_hand.append(deck.pop())
            dealer_score = 0
            for card in dealer_hand:
                rank = card[0]
                if rank == 'J' or rank == 'Q' or rank == 'K':
                    dealer_score += 10
                elif rank == 'A':
                    dealer_score += 11
                else:
                    dealer_score += int(rank)
            print("Dealer's hand:", dealer_hand)
            print("Dealer's score:", dealer_score)
