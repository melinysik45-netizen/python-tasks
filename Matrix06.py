#Matrix6 Даны M, N, число Q и набор из N чисел. Первая строка — набор; каждая следующая строка равна предыдущей, умноженной на Q по столбцам

m = int(input())
n = int(input())
q = int(input())
values = [int(x) for x in input().split()]
a = []
for i in range(m):
    row = []
    a.append(row)
    for j in range(n):
        row.append(values[j] * (q ** i))
for row in a:
    print(row)