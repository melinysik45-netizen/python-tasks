#Dict4. Построить словарь из N пар. Затем даны ключ K и число V: если K уже в словаре, увеличить его
#значение на V; если нет — добавить пару (K, V). Вывести итоговое значение ключа K.

n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
k = input()
v = int(input())
if k in d:
    d[k] = d[k] + v
else:
    d[k] = v
print(d[k])