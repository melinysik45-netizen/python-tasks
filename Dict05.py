#Dict5 Построить словарь из N пар. Удалить ключ K через pop с default: если ключа не было, словарь
#не меняется. Вывести размер после удаления

n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
k = input()
d.pop(k, None)
print(len(d))