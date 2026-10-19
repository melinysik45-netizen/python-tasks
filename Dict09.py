#Dict9 Построить словари из N и M пар. Слить второй в первый через update. Вывести размер
#результата и значение ключа, который был в обоих словарях (такой ключ гарантированно есть)

n = int(input())
d1 = {}
for i in range(n):
    key1 = input()
    value1 = int(input())
    d1[key1] = value1
m = int(input())
d2 = {}
for i in range(m):
    key2 = input()
    value2 = int(input())
    d2[key2] = value2
d1.update(d2)
print(len(d1))
common_key = input()
print(d1[common_key])