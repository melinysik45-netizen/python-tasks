#List9 Дан список A из N чисел. Вывести элементы, большие среднего арифметического всех элементов, и их количество

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
count = 0
average = sum(a) / len(a)
for x in a:
    if x > average:
        count += 1
        print(x)
print(count)