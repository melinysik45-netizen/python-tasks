#List15 Дан список A из N чисел. Вывести элементы на нечётных позициях (1, 3, 5… при счёте позиций с 1) и их сумму

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
summa = 0
for i in range(len(a)):
    if i % 2 == 0:
        print(a[i])
        summa += a[i]
print(summa)