#Matrix1. Даны целые положительные числа M и N. Сформировать целочисленную матрицу размера M × N, у которой все элементы I-й строки имеют значение 10·I (I = 1, …, M). 

m = int(input()) 
n = int(input()) 
a = [] 
for i in range(1, m + 1): 
    row = [] 
    for j in range(n): 
        row.append(10 * i) 
    a.append(row) 
for row in a: 
    print(row)
