#List27. Дан список из N строк-пар: урон героя и урон врага за раунд. Вывести строки в порядке убывания
#урона героя (key-лямбда по столбцу 0) и лучшую строку.

n = int(input())
rows = []
for i in range(n):
    x = float(input())
    y = float(input())
    rows.append([x, y])
rows.sort(key=lambda r: r[0], reverse=True)
for r in rows:
    print(r)
print(rows[0])