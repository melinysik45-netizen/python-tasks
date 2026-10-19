#Dict2 Построить словарь из N пар. Дан ключ K: вывести его значение, если K есть, иначе строку «нет
#такого ключа» (через in)

n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
k = input()
if k in d:
    print(d[k])
else:
    print("Такого ключа нет")