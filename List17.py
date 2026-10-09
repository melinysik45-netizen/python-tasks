#List27. Дан список из N строк-пар: урон героя и урон врага за раунд. Вывести строки в порядке убывания
#урона героя (key-лямбда по столбцу 0) и лучшую строку.
n = int(input())
a = []
for i in range(n):
    a.append(input().split())
sorted_a = sorted(a, key=lambda x: int(x[0]), reverse=True)
for row in sorted_a:
    print(row)
best_row = sorted_a[0]
print(best_row)