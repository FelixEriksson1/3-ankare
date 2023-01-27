import sys
import time
import random


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)


class spelare_info():
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def print_info(self):

        print("")

    def check_money(self):
        print("")


namn = input("Enter Your Username: ")
print("Welcome", namn)

player = spelare_info(namn, 400,)


def welocome():
    while True:
        global kasinot
        kasinot = (input("Do You Want To Enter The Casino? 1.Yes 2.No "))
        if kasinot == "1":
            print("Welcome To The Casino!")
            print_slow(
                "You Have 400 Dollars In Your Bank Account, You Have To Exchange Money Into Chips")
            break
        elif kasinot == "2":
            print_slow("Thanks For Playing")
            break
        else:
            print_slow("You Answer By Pressing 1 or 2")


def dollar_to_chip():
    player.check_money()
    Dollar = (int(input(f"How Much Money Do You Want to Exchange?:")))
    if -1 < Dollar < 401:
        player.money = Dollar
        print(f"{Dollar} Dollars have exchanged to {player.money} chips.")

    else:
        print_slow("Answer between 0-400")
        dollar_to_chip()


def spela():
    global turtle_värde
    if player.money < 0.000001:
        print("You Are Out Of Chips, Thanks for playing")
        time.sleep(14)
        sys.exit
    else:
        spel = (input(
            "What do you want to play? Press 1 to play horsebetting, 2 for BlackJack and 3 to exit "))
    if spel == "1":

        from turtle import Turtle, Screen

        def moneyreturn():
            bet_money = float(input("How much do you want to bet: "))
            if 0.0000001 > bet_money or bet_money > player.money:
                print_slow(
                    "You cant bet more chips or you are out of chips")
                moneyreturn()
            else:

                print(
                    "You can choose from: 'White' 'Red' 'Orange' 'Pink' 'Tomato' 'Dodgerblue' 'Yellow'")
                time.sleep(2)
                bet_turtle = (input("What horse do you want to bet on: "))

                screen = Screen()
                screen.setup(width=800, height=600)
                screen.bgpic('road.gif')

                y_positions = [-260, -172, -85, 2, 85, 172, 260]
                color = ["white", "red", "orange", "pink",
                         "tomato", "dodgerblue", "yellow"]
                all_turtle = []
                for index in range(0, 7):
                    new_turtle = Turtle(shape="turtle")
                    new_turtle.shapesize(2)
                    new_turtle.speed('fastest')
                    new_turtle.penup()
                    new_turtle.goto(x=-350, y=y_positions[index])
                    new_turtle.color(color[index])
                    all_turtle.append(new_turtle)

                on = True

                while on:
                    for turtle in all_turtle:
                        if turtle.xcor() > 330:
                            on = False
                            winner = turtle.pencolor()
                            if winner == bet_turtle:
                                print(f"You won! {winner} Came in First!")
                                bet_money = bet_money*5
                                player.money += bet_money

                            else:
                                print(f'You lost! {winner} Came in first!')
                                player.money -= bet_money
                        random_speed = random.randint(0, 18)
                        turtle.forward(random_speed)
                print(f"You have {player.money} chips now")
                screen.exitonclick()
                spela()
        moneyreturn()
    elif spel == "3":
        print("Thanks for playing")
    elif spel == "2":
        deck = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7',
                 '8', '9', '10', 'J', 'Q', 'K', 'A']
        for suit in suits:
            for rank in ranks:
                card = rank + ' of ' + suit
                deck.append(card)
        replay = False

        while True:
            if replay == False:
                bet = int(input("How much do you want to bet?"))
                if bet > player.money:
                    print("You dont have enough chips to do that.")
            else:
                print("Do you want to play again \n Y/N")
                replay_bet = input()
                if replay_bet == "N" or replay_bet == "n":
                    spel = (input("Do you want to play again? 1. Yes 2. No"))
                    if spel == "1":
                        spela()
                        break

            # Inbyggd funktion som shufflar kortleken
            random.shuffle(deck)

            # Ger två kort till spelaren och dealern
            player_hand = [deck.pop(), deck.pop()]
            dealer_hand = [deck.pop(), deck.pop()]

            # Räknar ut poäng
            player_score = 0
            for card in player_hand:
                rank = card[0]
                if rank == 'J' or rank == 'Q' or rank == 'K' or rank == '1':
                    player_score += 10
                elif rank == 'A':
                    player_score += 11
                else:
                    player_score += int(rank)

            dealer_score = 0
            for card in dealer_hand:
                rank = card[0]
                if rank == 'J' or rank == 'Q' or rank == 'K' or rank == '1':
                    dealer_score += 10
                elif rank == 'A':
                    dealer_score += 11
                else:
                    dealer_score += int(rank)

            # Kollar efter blackjack
            if player_score == 21:
                print("Player has blackjack and wins!")
            elif dealer_score == 21:
                print("Dealer has blackjack and wins!")
            else:
                # spelarens drag
                while True:
                    print("Players Hand", player_hand)
                    print(player_score)
                    choice = input("Do you want to hit or stand?")
                    if choice == 'hit':
                        player_hand.append(deck.pop())
                        player_score = 0
                        for card in player_hand:
                            rank = card[0]
                            if rank == 'J' or rank == 'Q' or rank == 'K' or rank == "1":
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

                # dealerns drag
                if player_score <= 21:
                    while dealer_score < 17:
                        dealer_hand.append(deck.pop())
                        dealer_score = 0
                        for card in dealer_hand:
                            rank = card[0]
                            if rank == 'J' or rank == 'Q' or rank == 'K' or rank == "1":
                                dealer_score += 10
                            elif rank == 'A':
                                dealer_score += 11
                            else:
                                dealer_score += int(rank)
            print("Dealer's hand:", dealer_hand)
            print("Dealer's score:", dealer_score)

            if player_score > dealer_score and player_score < 21 or dealer_score > 21:
                print("Player Wins")
                print("You win", str(bet))
                player.money += bet
                print("Din balance är", player.money)
            else:
                player.money -= bet
                print("Dealer Wins")
            replay = True


welocome()


if kasinot == "1":
    dollar_to_chip()
    spela()
