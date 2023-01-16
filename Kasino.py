class spelare_info():
    def __init__(self, name, money, level):
        self.name = name
        self.money = money
        self.level = level

    def print_info(self):

        print(
            f"Your name {self.name}. Your money {self.money}. Your level {self.level}.")

    def chek_money(self):
        print(f"You have {self.money} dollar.")


namn = input("What's your username?")
print("Welcome", namn)

player = spelare_info(namn, 400, 1)


while True:
    kasinot = (input(
        "Do you wish to enter the casino? -->1.Yes 2. No "))
    if kasinot == "1":
        print("Welcome to the casino!")
        print("För att spela i kasinot måste du växla dinna pengar till marker.")

        while True:
            def dollar_to_chip():
                player.chek_money()
                Dollar = float(
                    input(f"Ange antalet dollar du vill växla till kasinomarker:"))
                if 0 < Dollar < 400:
                    amount_in_casino = Dollar
                    player.money = player.money - amount_in_casino
                    print(
                        f"{Dollar} Dollar is converted to {amount_in_casino} casinochips .")

                else:
                    print("Ange ditt svar i siffror mellan 0-400")

            dollar_to_chip()
    elif kasinot == "2":
        print("Thanks for playing.")
        break
    else:
        print("You awnser by typing 1 or 2")
