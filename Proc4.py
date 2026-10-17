#Proc4 Функция triangle_ps(a) возвращает периметр P = 3·a и площадь S = a2·√3/4 равностороннего
#треугольника. Найти P и S трёх данных сторон

import math

def triagle_ps(a):
    perimetr = 3 * a
    Area = (a ** 2 * math.sqrt(3)) / 4
    return perimetr, Area
for i in range(3):
    a = float(input())
    print(triagle_ps(a))