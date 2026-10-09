#List25 Дан список A из N различных чисел. Вывести второй по величине элемент 

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
sorted_a = sorted(a)
print(sorted_a[-2])