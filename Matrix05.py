#Matrix5 Даны M, N, число D и набор из M чисел. Первый столбец — набор; каждый следующий столбец равен предыдущему плюс D по строкам

m = int(input())
n = int(input())
d = int(input())
a = []
values = [int(x) for x in input().split()]
for i in range(m):
    row = []
    a.append(row)
    for j in range(n):
        row.append(values[i] + d * j)
for row in a:
    print(row)