#List14 Дан список A из N чисел и число D. Вывести число вхождений D (count) и индекс первого вхождения (или -1, если D нет)

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
d = int(input())
count = a.count(d)
if d in a:
    index_d = a.index(d)
else:
    index_d = -1
print(count)
print(index_d)