#Proc18 Функция circle_s(r) возвращает площадь круга радиуса r (π = 3.14). Найти площади трёх кругов

def circle_s(r):
    S = 3.14 * r ** 2
    return S
for i in range(3):
    r = float(input())
    print(circle_s(r))