from abc import ABC, abstractmethod

# Шаг 1: Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализация конкретных типов оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом"

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука"


# Шаг 3: Класс Боец
class Fighter:
    def __init__(self, name: str):
        self.name = name
        self.weapon: Weapon = None

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.__class__.__name__.lower()}")

    def attack(self):
        if self.weapon:
            print(self.weapon.attack())
        else:
            print(f"{self.name} без оружия не может атаковать.")

# Класс Монстр
class Monster:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def take_damage(self):
        print(f"Монстр {self.name} побеждён!")

# Шаг 4: Реализация боя
def battle(fighter: Fighter, monster: Monster):
    print(f"Бой начинается между бойцом {fighter.name} и монстром {monster.name}")
    fighter.attack()
    monster.take_damage()

fighter = Fighter("кот Васька")
monster = Monster("Дракоша", 100)

# Боец выбирает меч
fighter.changeWeapon(Sword())
battle(fighter, monster)

# Боец выбирает лук
fighter.changeWeapon(Bow())
battle(fighter, monster)
