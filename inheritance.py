# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name}, protector of {self.city} with the power of {self.power}!")

    def fight_crime(self):
        print(f"{self.name} is fighting crime!")

# Inherited class with added attributes and overridden method
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    # Polymorphism: overriding fight_crime
    def fight_crime(self):
        print(f"{self.name} flies at {self.flight_speed} km/h to fight crime!")

# Using the classes
hero1 = Superhero("Strongman", "Super Strength", "Metro City")
hero2 = FlyingSuperhero("Sky Flash", "Flight & Speed", "Skyline", 300)

hero1.introduce()
hero1.fight_crime()

hero2.introduce()
hero2.fight_crime()
