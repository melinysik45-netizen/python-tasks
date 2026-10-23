#Matrix3 Даны M, N и набор из M чисел. Сформировать матрицу, у которой в каждом столбце содержатся все числа набора в том же порядке

m = int(input())
n = int(input())
a = []
values = [int(x) for x in input().split()]
for i in range(m):
    row = []
    a.append(row)
    for j in range(n):
        row.append(values[i])
for row in a:
    print(row)