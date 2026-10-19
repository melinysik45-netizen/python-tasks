#Dict1. Построить словарь из N пар (строка-ключ, целое значение). Вывести число пар и все ключи в
#порядке добавления.

n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
print(len(d))
for key in d:
    print(key)