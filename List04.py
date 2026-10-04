#List4. Дан список A из N чисел. Найти его максимальный элемент и индекс (с 0). Вывести сначала индекс, затем элемент. 
n = int(input()) 
a = [] 
for i in range(n): 
    a.append(int(input())) 
imax = 0 
for i in range(len(a)): 
    if a[i] > a[imax]: 
        imax = i 
print(imax) 
print(a[imax])
