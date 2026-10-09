#List26 Дан список A из N чисел. Генератором вывести элементы, большие среднего, и само среднеe
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
avg = sum(a) / len(a)
generator = [x for x in a if x >= avg]
print(avg)
print(generator)
