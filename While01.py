# While1. Даны положительные A и B (A > B). Не используя * и /,
# найти длину незанятой части отрезка A после укладки отрезков B.

a = int(input())
b = int(input())

free = a
while free >= b:
 free -= b

print(free)