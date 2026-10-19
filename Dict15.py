#Dict15 Построить словари из N и M пар. Добавить в первый пары второго без update: только ключи,
#которых нет; совпавшие ключи считать проигнорированными. Вывести размер и число
#проигнорированных
n = int(input())
d1 = {}
for i in range(n):
    key = input()
    value = int(input())
    d1[key] = value
m = int(input())
d2 = {}
for i in range(m):
    key = input()
    value = int(input())
    d2[key] = value
ignored_count = 0
for key, value in d2.items():
    if key in d1:
        ignored_count += 1
    else:
        d1[key] = value
print(len(d1))
print(ignored_count)