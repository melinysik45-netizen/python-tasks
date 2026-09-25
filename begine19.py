#Begin19 Даны координаты двух противоположных вершин прямоугольника: (x1, y1), (x2, y2). 
#Стороны прямоугольника параллельны осям координат. Найти периметр и площадь данного прямоугольника.
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

widht = abs(x2 - x1)
height = abs(y2 - y1)

perimetr = 2 * (widht + height)
area = widht * height

print(perimetr)
print(area)