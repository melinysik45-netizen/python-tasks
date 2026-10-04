#List5 Дан список A из N чисел и число D. Добавить D в конец (append), вывести новый список и его длину

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
d = int(input())
a.append(d)
print(a)
print(len(a))