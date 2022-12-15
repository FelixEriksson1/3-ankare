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


namn = input("What's your username? ")
print("Welcome", namn)

player = spelare_info(namn, 400, 1)


kasinot = int(input(
    "Do you wish to enter the casino? -->(yes/no)"))
if kasinot == 1:
    print("Welcome to the casino!")
    player.chek_money()
else:
    print("Thanks for playing.")

Dollar = float(input("Ange antalet dollar du vill växla till kasinomarker: "))

amount_in_casino = Dollar * 1

print(f"{Dollar} Dollar is converted {amount_in_casino} casinochips .")
