def days_indexes(self, day):
    day = f" Today the {day} of {self.name}'s life "
    print(f"{day:=^50}","\n")
    human_indexes = self.name + "'s indexes"
    print(f"{human_indexes:^50}","\n")
    print(f"Money – {self.money}")
    print(f"Satiety – {self.satiety}")
    print(f"Gladness – {self.gladness}")
    home_indexes = "Home indexes"
    print(f"{home_indexes:^50}", "\n")
    print(f"Food – {self.home.food}")
    print(f"Mess – {self.home.mess}")
    car_indexes = f"{self.car.brand} car indexes"
    print(f"{car_indexes:^50}", "\n")
    print(f"Fuel – {self.car.fuel}")
    print(f"Strength – {self.car.strength}")