#Class7 Класс Point с методом __str__, возвращающим «(x, y)»; вывести точку одним print

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

x = int(input("Введите x: "))
y = int(input("Введите y: "))
p = Point(x, y)

print(p)
