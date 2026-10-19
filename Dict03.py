#Dict3 Построить словарь из N пар. Дан ключ K: вывести значение через get с default 0 одной строкой

n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
k = input()
print(d.get(k, 0))