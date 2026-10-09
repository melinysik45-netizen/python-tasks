#List22 Дан список A из N чисел и число D. Генератором вывести элементы, умноженные на D, и
#количество элементов, равных D

n = int(input())
d = int(input())
a = []
for i in range(n):
    a.append(int(input()))
multiplied_a = [x * d for x in a]
print(multiplied_a)
print(a.count(d))