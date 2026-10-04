#List8. Дан список A из N чисел и число D. Удалить первое вхождение D; если D нет в списке — вывести список без изменений. Вывести полученный список и его длину. 
n = int(input()) 
a = [] 
for i in range(n): 
    a.append(int(input())) 
d = int(input()) 
if d in a: 
    a.remove(d) 
print(a) 
print(len(a))
