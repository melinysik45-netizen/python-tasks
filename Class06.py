#Class6 Класс Inventory: словарь предметов в __init__; методы add(name, qty) и total() (сумма
#количеств); вывести total после трёх добавлений

class Inventory:
    def __init__(self):
        self.items = {}

    def add(self, name, qty):
        self.items[name] = self.items.get(name, 0) + qty

    def total(self):
        return sum(self.items.values())

inventory = Inventory()

for i in range(3):
    item_name = input(f"Название предмета {i+1}: ")
    quantity = int(input(f"Количество {i+1}: "))
    inventory.add(item_name, quantity)

print(inventory.total())
