#Begin18 Даны три точки A, B, C на числовой оси. Точка C расположена между точками A
#и B. Найти произведение длин отрезков AC и BC.
A = float(input())
B = float(input())
C = float(input())

AC = abs(C - A)
BC = abs(C - B)
product = AC * BC

print(product)