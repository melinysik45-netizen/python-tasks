#List21 Дан список A из N чисел. Генератором с фильтром вывести только положительные элементы и
#их количество

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
positiv_nomber = [x for x in a if x > 0]
print(positiv_nomber)
print(len(positiv_nomber))
