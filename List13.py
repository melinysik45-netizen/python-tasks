#List13 Дан список A из N чисел. Удалить последний элемент (pop), вывести удалённый элемент и полученный список

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
delete = a.pop()
print(delete)
print(a)