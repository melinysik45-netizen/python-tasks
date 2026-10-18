#Proc5 Функция rect_ps(x1, y1, x2, y2) возвращает периметр и площадь прямоугольника со сторонами,
#параллельными осям, по противоположным вершинам. Найти P и S трёх прямоугольников

def rect_ps(x1, y1, x2, y2):
    width = abs(x1 - x2)
    height = abs(y1 - y2)
    Perimetr = (width + height) * 2
    Area = width * height
    return Perimetr, Area
for i in range(3):
    x1 = float(input())
    x2 = float(input())
    y1 = float(input())
    y2 = float(input())
    print(rect_ps(x1, y1, x2, y2))
