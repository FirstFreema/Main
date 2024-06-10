class Wine:
    def __init__(self, volume, type, year, color):
        self.volume = volume
        self.type = type
        self.year = year
        self.color = color

    def get_drink(self):
        answer = input(f"Вы хотите выпить это {self.type} вино {self.year} года? (да/нет) ")
        if answer.lower() == "да":
            print("Вы выпили вино.")
        else:
            print("Вы не стали пить вино.")

    def get_pour_glass(self):
        answer = input(f"Вы хотите налить себе бокал {self.type} вина {self.year} года? (да/нет) ")
        if answer.lower() == "да":
            print("Вы налили себе бокал вина.")
        else:
            print("Вы не стали наливать вино в бокал.")

    def get_use(self):
        answer = input(f"Вы хотите использовать это {self.type} вино {self.year} года для приготовления пищи? (да/нет) ")
        if answer.lower() == "да":
            print("Вы использовали вино для приготовления пищи.")
        else:
            print("Вы не стали использовать вино для приготовления пищи.")

    def get_decanter(self):
        answer = input(f"Вы хотите перелить {self.type} вино {self.year} года в декантер? (да/нет) ")
        if answer.lower() == "да":
            print("Вы перелили вино в декантер.")
        else:
            print("Вы не стали переливать вино в декантер.")

# Проверка
wine1 = Wine(750, "Каберне Совиньон", 2019, "красное")
wine2 = Wine(500, "Шардоне", 2021, "белое")

wine1.get_drink()
wine1.get_pour_glass()
wine1.get_use()
wine1.get_decanter()

wine2.get_drink()
wine2.get_pour_glass()
wine2.get_use()
wine2.get_decanter()
