#List2  Дан список A из N чисел и индекс K (с 0). Вывести A[K], последний элемент и число элементов перед элементом с индексом K

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = int(input())
print(a[k])
print(a[-1])
print(k)