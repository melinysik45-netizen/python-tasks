#List16. Дан список из N чисел. Вывести сумму, минимум и максимум его элементов, пользуясь sum, min,
#max

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
print(sum(a))
print(min(a))
print(max(a))