import os
os.system ("cls")
class Character:
    def __init__(self, name, health = 100):
        self.name = name
        self.health = health
    def introduce(self):
        print(f"I am {self.name}.")
    def take_damage(self, amount):
        self.health = self.health - amount
        print(f"{self.name} took {amount} damage. Health is now {self.health}.")
    def is_alive(self):
        return True if self.health > 0 else False
    def describe_role(self):
        print("I am just a generic character.")


class Warrior(Character):
    def __init__(self, name, weapon, health = 100):
        super().__init__(name, health)
        self.weapon = weapon
    def attack(self):
        print(f"{self.name} attacks with a {self.weapon}!")
    def describe_role(self):
        print("Warrior-Specific")


class Mage(Character):
    def __init__(self, name , mana = 50 , health = 100):
        super().__init__(name, health)
        self.mana = mana
    def cast_spell(self):
        print(f"{self.name} casts a spell!")
    def describe_role(self):
        print("Mage-Specific")


class Paladin(Warrior):
    def __init__(self, name, weapon, faith,  health = 100):
        super().__init__(name, weapon, health)
        self.faith = faith
    def smite(self):
        super().attack()
        print(f"{self.name} channels holy power!")
    def describe_role(self):
        print("Paladin-Specific")



class Building:
    def __init__(self, durability = 100):
        self.durability = durability
    def repair(self, amount):
        self.durability = amount + self.durability

class GuardTower(Warrior, Building):
    def __init__(self, name, weapon, durability = 100):
        Warrior.__init__(self, name, weapon)
        Building.__init__(self, durability)

