#Dict7 Построить словарь из N пар. Вывести ключ с наибольшим значением (перебор с кандидатом;
#значения различны)

n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
key_list = list(d)
best_key = key_list[0]
for key in d:
    if d[key] > d[best_key]:
        best_key = key
print(best_key)