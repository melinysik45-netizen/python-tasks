#Class1. Описать класс Point с полями x и y, задаваемыми в __init__. Прочитать две координаты, создать
#точку, вывести поля по строке.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
x = int(input())
y = int(input())
p = Point(x, y)
print(p.x)
print(p.y)