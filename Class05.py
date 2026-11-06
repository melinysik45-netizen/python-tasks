#Class5. Описать класс Point из Class1. Прочитать N точек и вывести координаты точки с наибольшим x
#через max с key-лямбдой.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
n = int(input())
points = []
for i in range(n):
    x = int(input())
    y = int(input())
    points.append(Point(x, y))
best = max(points, key=lambda p: p.x)
print(best.x)
print(best.y)