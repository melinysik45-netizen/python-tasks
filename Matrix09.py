#Matrix9. Дана матрица размера M × N. Вывести её элементы, расположенные в строках с чётными номерами (2, 4, …). Вывод производить по строкам, условный оператор не использовать. 

m = int(input()) 
n = int(input()) 
a = [] 
for i in range(m): 
    row = [int(x) for x in input().split()] 
    a.append(row) 
for row in a[1::2]: 
    print(row)
