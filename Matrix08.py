#Matrix8. Дана матрица размера M × N и целое K (1 ≤ K ≤ N). Вывести элементы K-го столбца данной матрицы. 

m = int(input()) 
n = int(input()) 
a = [] 
for i in range(m): 
    row = [int(x) for x in input().split()] 
    a.append(row) 
k = int(input()) 
print([row[k - 1] for row in a])
