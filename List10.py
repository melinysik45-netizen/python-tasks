#List10 Дан список из N строк. Вывести самую длинную и самую короткую строку (первую из встретившихся) и их длины

n = int(input())
a = []
for i in range(n):
    a.append(input())
max_str = a[0]
min_str = a[0]
max_len = len(a[0])
min_len = len(a[0])
for x in a:
    if len(x) > max_len:
        max_str = x
        max_len = len(x)
    elif len(x) < min_len:
        min_str = x
        min_len = len(x)
print(max_len)
print(max_str)
print(min_len)
print(min_str)