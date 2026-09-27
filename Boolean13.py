#Boolean13 Даны три целых числа: A, B, C. Проверить истинность высказывания: «Хотя бы
#одно из чисел A, B, C положительное».

a = int(input())
b = int(input())
c = int(input())

print(a > 0 or b > 0 or c > 0)