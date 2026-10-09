#List28 Дан список из N строк и буква. Генератором вывести строки, начинающиеся с этой буквы
#(первый символ строки)

n = int(input())
letter = input()
a = []
for i in range(n):
    a.append(input())
generator = [x for x in a if x[0] == letter]
print(generator)