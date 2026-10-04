#list01 Дан список из N чисел. вывести его длину и первый элемент

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
print(len(a))
print(a[0])