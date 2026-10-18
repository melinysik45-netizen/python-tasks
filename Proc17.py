#Proc17 Функция roots_count(a, b, c) возвращает число корней квадратного уравнения по
#дискриминанту D = b2 − 4·a·c (a ≠ 0). Найти количество корней трёх уравнений

def roots_count(a, b, c):
    D = b ** 2 - 4 * a * c
    if D > 0:
        return 2
    if D == 0:
        return 1
    return 0


for i in range(3):
    a = float(input())
    b = float(input())
    c = float(input())
    print(roots_count(a, b, c))