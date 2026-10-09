#List18. Дан список A из N чисел. Отсортировать его на месте по убыванию и вывести список и его длину.

n = int(input())
a = []

for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)
print(a)
print(len(a))