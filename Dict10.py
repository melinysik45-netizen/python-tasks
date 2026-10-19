#Dict10. Построить словарь из N пар (название предмета, цена). Вывести каждую пару строкой «название:
#цена» через перебор items с распаковкой.

n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
for name, price in d.items():
    print(f"{name}: {price}")