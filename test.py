import random

# Lista med kortlekens kort
kortlek = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
kläddakort = ["Knäckt", "Dam", "Kung", "Ess"]

# Funktion som slumpar ett kort från kortleken och returnerar det


def slumpa_kort():
    return random.choice(kortlek)


# Spelarens hand
hand = []

# Dealerns hand
dealer = []

# Börja spelet
print("Välkommen till Blackjack!")

# Dealern slumpar ett kort till spelaren och ett till sig själv
hand.append(slumpa_kort())
dealer.append(slumpa_kort())

# Dealern slumpar ytterligare ett kort till sig själv, men visar det inte
dealer.append(slumpa_kort())

spelare_poang = 0
for card in hand:
    rank = card[0]
    if rank == 'J' or rank == 'Q' or rank == 'K':
        spelare_poang += 10
    elif rank == 'A':
        spelare_poang += 11
    else:
        spelare_poang += int(rank)

dealer_score = 0
for card in hand:
    rank = card[0]
    if rank == 'J' or rank == 'Q' or rank == 'K':
        dealer_score += 10
    elif rank == 'A':
        dealer_score += 11
    else:
        dealer_score += int(rank)


if spelare_poang == 21:
    print("Player has blackjack and wins!")
elif dealer_score == 21:
    print("Dealer has blackjack and wins!")
else:
    print("Din hand:", hand)

# Spelaren får välja om de vill dra ett till kort eller stanna
while True:
    val = input("Vill du dra ett till kort? (j/n)")
    if val.lower() == 'j':
        hand.append(slumpa_kort())
        print("Din hand:", hand)
    else:
        break

# Räkna ut poängen för spelarens och dealerns hand


def poang(hand):
    poang = 0
    ess = 0
    for kort in hand:
        if kort in ['J', 'Q', 'K']:
            poang += 10
        elif kort == 'A':
            ess += 1
            poang += 11
        else:
            poang += int(kort)
    # Kolla om spelaren fått över 21 poäng och om så är fallet, för ner ett ess till 1 poäng
    while poang > 21 and ess > 0:
        poang -= 10
        ess -= 1
    return poang


if hand == 21:
    print("Player has blackjack and wins!")
elif hand == 21:
    print("Dealer has blackjack and wins!")
else:
    # player's turn
    while True:
        choice = input("Do you want to hit or stand? ")
        if choice == 'hit':
            hand.append(kortlek.pop())
            spelare_poang = 0
            for card in hand:
                rank = card[0]
                if rank == 'J' or rank == 'Q' or rank == 'K':
                    spelare_poang += 10
                elif rank == 'A':
                    spelare_poang += 11
                else:
                    spelare_poang += int(rank)
            print("Player's hand:", hand)
            print("Player's score:", spelare_poang)
            if spelare_poang > 21:
                print("Player busts and loses.")
                break
        elif choice == 'stand':
            break
        else:
            print("Invalid choice. Please enter hit or stand.")

# Visa dealerns hand och poäng
print("Dealerns hand:", dealer)
print("Dealerns poäng:", poang(dealer))

# Räkna ut vem som vann
spelarns_poang = poang(hand)
dealerns_poang = poang(dealer)
if spelarns_poang > 21:
    print("Du förlorade!")
elif dealerns_poang > 21 or spelarns_poang > dealerns_poang:
    print("Du vann!")
else:
    print("Du förlorade!")
