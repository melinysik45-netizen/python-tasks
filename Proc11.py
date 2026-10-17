#Proc11 Функция minmax(x, y) возвращает пару (меньшее, большее). Четырьмя вызовами найти
#минимум и максимум четырёх данных чисел A, B, C, D

def minmax(x, y):
    if x < y:
        return x, y
    else:
        return y, x

a = int(input())
b = int(input())
c = int(input())
d = int(input())

min1, max1 = minmax(a, b)
min2, max2 = minmax(c, d)
absolut_min, _ = minmax(min1, min2)
_, absolut_max = minmax(max1, max2)
print(f"Минимальное число: {absolut_min}")
print(f"Максимальное число: {absolut_max}")