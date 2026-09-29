#Дано вещественное число — цена 1 кг конфет. Вывести стоимость 0.1, 0.2, ..., 1
#кг конфет.

price = float(input())

for i in range(1, 11):
    weight = i / 10

print(f"{price * i:.2f}")
