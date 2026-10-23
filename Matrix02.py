#Matrix2 Сформировать матрицу M × N, у которой все элементы J-го столбца равны 5·J (J = 1, …, N)

m = int(input())
n = int(input())
a = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(5 * (j + 1))
    a.append(row)
for row in a:
    print(row)