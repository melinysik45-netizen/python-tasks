#Matrix4. Даны целые положительные числа M, N и набор из N чисел. Сформировать матрицу размера M × N, у которой в каждой строке содержатся все числа исходного набора в том же порядке. 

m = int(input()) 
n = int(input()) 
values = [int(x) for x in input().split()] 
a = [] 
for i in range(m): 
    a.append(values[:]) 
for row in a: 
    print(row)
