#List19 Дан список из N строк. Вывести строки в порядке возрастания длины и отдельно самую
#длинную (max с key)

n = int(input())
a = []
for i in range(n):
    a.append(input())
sorted_a = sorted(a, key=len)
print(sorted_a)
print(max(sorted_a, key=len))