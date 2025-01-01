class Animal:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def __str__(self):
        return f"{self.name} is {self.age} years old and weighs {self.weight} kg."
        
    def eat(self):
        return f"{self.name} is eating."
    
    def sleep(self):
        return f"{self.name} is sleeping."


class Cow(Animal):

    def __init__(self, name, age, weight, milk_production):
        super().__init__(name, age, weight)
        self.milk_production = milk_production
    
    def produce_milk(self):
        return f"{self.name} produces {self.milk_production} litres of milk per day."
    
    
class Chicken(Animal):
    def __init__(self, name, age, weight, eggs_laid):
        super().__init__(name, age, weight)
        self.eggs_laid = eggs_laid

    def lay_eggs(self):
        print(f"{self.name} lays {self.eggs_laid} eggs per day.")


class Sheep(Animal):
    def __init__(self, name, age, weight, wool_production):
        super().__init__(name, age, weight)
        self.wool_production = wool_production

    def produce_wool(self):
        print(f"{self.name} produces {self.wool_production} kg of wool per year.")

