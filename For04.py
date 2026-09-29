#For4 Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1, 2, ..., 10 кг
#конфет.

price = float(input())

for kg in range(1, 11):
    print(f"{price * kg:.2f}")