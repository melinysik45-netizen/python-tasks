#List24. Дан список из N строк. Вывести строки в порядке возрастания длины (sorted с key=len) и отдельно
#— самую длинную строку (max с key=len)

n = int(input())
s = []
for i in range(n):
    s.append(int(input()))
print(sorted(s, key=len))
print(max(s, key=len))