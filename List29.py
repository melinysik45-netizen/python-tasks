#List29 Дан список A из N чисел и число K. Вывести K наибольших элементов в порядке убывания
#(сортировка плюс срез)

n = int(input())
k = int(input())
a = []
for i in range(n):
    a.append(int(input()))
sorted_a = sorted(a, reverse=True)
print(sorted_a[0:k])