#List3  Дан список A из N чисел. Вывести сумму элементов и произведение элементов с чётными индексами (0, 2, 4…)

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
summa = 0
product = 1
for i in range(len(a)):
    summa += a[i]
    if i % 2 == 0:
        product *= a[i]
print(summa)
print(product)