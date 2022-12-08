class spelare_info():
    def __init__(self, name, money, level):
        self.name = name
        self.money = money
        self.level = level

    def print_info(self):

        print(
            f"Ditt namn {self.name}. Dinna pengar {self.money}. Din level {self.level}.")

    def chek_money(self):
        print(f"Du har {self.money} dollar.")


namn = input("Vad är ditt namn? ")
print("Hej", namn)

player = spelare_info(namn, 400, 1)


kasinot = int(input(
    "1.Vill du gå in i kasinot tryk 1. 2. Vill du avsluta tryck 2. -->"))
if kasinot == 1:
    print("välkomen till kasinot!")
    player.chek_money()
else:
    print("Tack för att du spela.")
