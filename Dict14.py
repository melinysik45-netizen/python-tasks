#Dict14 Построить словарь из N пар и число V. Удалить все пары со значением меньше V, не меняя
#словарь во время перебора. Вывести размер после удаления

n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
v = int(input())
for key in list(d):
    if d[key] < v:
        del d[key]
print(len(d))