#If5 Даны три целых числа. Найти количество положительных и количество отрицательных чисел в исходном наборе.

a = int(input())
b = int(input())
c = int(input())

count_positiv = (a > 0) + (b > 0) + (c > 0)
count_negative = (a < 0) + (b < 0) + (c < 0)

print(count_positiv)
print(count_negative)