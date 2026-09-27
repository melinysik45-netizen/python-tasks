#Boolean7 Даны три целых числа: A, B, C. Проверить истинность высказывания: «Число B
#находится между числами A и C».

a = int(input())
b = int(input())
c = int(input())

print(a <= b <= c or c <= b <= a)