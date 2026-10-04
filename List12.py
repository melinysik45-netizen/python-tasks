#List12 Дан список A из N чисел и индекс K (0 ≤ K ≤ N). Вставить 0 в позицию K (insert), вывести список и длину


n = int(input())
a = []
for i  in range(n):
    a.append(int(input()))
k = int(input())
a.insert(k, 0)
print(a)
print(len(a))