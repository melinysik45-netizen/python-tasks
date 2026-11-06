#Class2 К классу Point добавить метод shift(dx, dy), меняющий координаты; применить и вывести поля

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def shift(self, dx, dy):
        self.x += dx
        self.y += dy

x = int(input("Введите x: "))
y = int(input("Введите y: "))
p = Point(x, y)

dx = int(input("Введите dx: "))
dy = int(input("Введите dy: "))

p.shift(dx, dy)

print(p.x)
print(p.y)
