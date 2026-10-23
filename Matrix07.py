#Matrix7. Дана матрица размера M × N и целое K (1 ≤ K ≤ M). Вывести элементы K-й строки данной матрицы.

m = int(input()) 
n = int(input()) 
a = [] 
for i in range(m): 
    row = [int(x) for x in input().split()] 
    a.append(row) 
k = int(input()) 
print(a[k - 1])
