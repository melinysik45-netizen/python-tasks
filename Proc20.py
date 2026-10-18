#Proc20 Функция triangle_p(a, h) возвращает периметр равнобедренного треугольника по основанию a
#и высоте h к основанию; боковая сторона b2 = (a/2)2 + h2. Найти периметры трёх треугольников

def triangle_p(a, h):
    b = ((a / 2) ** 2 + h ** 2) ** 0.5
    Perimetr = a + 2 * b
    return Perimetr
for i in range(3):
    a = float(input())
    h = float(input())
    print(triangle_p(a, h))