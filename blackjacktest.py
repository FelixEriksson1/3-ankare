import random

# Listan med kortleken
kortlek = ["2", "3", "4", "5", "6", "7", "8", "9", "10" 'J', 'Q', 'K', 'A']
Kläddakort = ["Knäckt", "Dam", "Kung", "ess"]

# Funktionen för att ge spelaren ett kort


def ge_kort():
    return random.choice(kortlek)


# Spelarens poäng
poang = 0

# Ge spelaren ett kort och lägg till poängen
poang += ge_kort()

# Ge spelaren ytterligare ett kort
poang += ge_kort()

# Skriv ut spelarens poäng
print("Du har " + str(poang) + " poäng.")

# Be spelaren om ett val
val = input("Vill du dra ett till kort? (j/n) ")

# Så länge spelaren väljer att dra ett till kort
while val.lower() == "j":
    # Ge spelaren ett till kort och lägg till poängen
    poang += ge_kort()

    # Skriv ut spelarens poäng
    print("Du har " + str(poang) + " poäng.")

    # Be spelaren om ett val igen
    val = input("Vill du dra ett till kort? (j/n) ")

# Kontrollera om spelaren har gått över 21 poäng
if poang > 21:
    print("Du har förlorat!")
else:
    print("Du har vunnit!")
