#List11. Дан список A из N чисел. Заменить все отрицательные элементы нулями и вывести полученный список и число заменённых элементов.

n = int(input()) 
a = [] 
for i in range(n): 
    a.append(int(input())) 
k = 0 
for i in range(len(a)): 
    if a[i] < 0: 
        a[i] = 0 
        k = k + 1 
print(a) 
print(k)
