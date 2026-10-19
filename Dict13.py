#Dict13 Построить словарь из N троек: название, цена, количество (значение — список из двух чисел).
#Вывести суммарную стоимость склада и название самого дорогого по стоимости предмета

n = int(input())
sklad = {}
for i in range(n):
    name = input()
    price = int(input())
    qty = int(input()) #колтчество
    sklad[name] = [price, qty]
total_sum = 0
max_cost = -1
most_expensive_name = ""
for name, info in sklad.items():
    price = info[0]
    qty = info[1]
    item_cost = price * qty
    total_sum += item_cost
    if item_cost > max_cost:
        max_cost = item_cost
        most_expensive_name = name

print(total_sum)
print(most_expensive_name)