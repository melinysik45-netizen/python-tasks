#Class8 Класс Hero: name, health, damage; методы to_dict() и from_dict(data); сохранить объект в
#словарь, создать из словаря новый объект и вывести его health

class Hero:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def to_dict(self):
        return {
            "name": self.name,
            "health": self.health,
            "damage": self.damage
        }

    @staticmethod
    def from_dict(data):
        return Hero(data["name"], data["health"], data["damage"])

name = input("Имя героя: ")
health = int(input("Здоровье героя: "))
damage = float(input("Урон героя: "))
hero_1 = Hero(name, health, damage)

saved_data = hero_1.to_dict()

hero_2 = Hero.from_dict(saved_data)

print(hero_2.health)
