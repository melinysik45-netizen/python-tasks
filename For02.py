#For2 Даны два целых числа A и B (A < B). Вывести в порядке возрастания все целые
#числа, расположенные между A и B (включая сами числа A и B), а также
#количество N этих чисел.

a = int(input())
b = int(input())

count = 0

for i in range(a, b + 1):
    print(i)
    count += 1

print(count)
