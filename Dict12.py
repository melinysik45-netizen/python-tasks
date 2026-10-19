#Dict12 Построить словарь из N пар с различными значениями. Построить обращённый словарь:
#значение ключ. Вывести его пары в порядке добавления исходного

n = int(input())
d = {}
inv_d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
for key, value in d.items():
    inv_d[value] = key
for new_key, new_value in inv_d.items():    
    print(f"{new_key}: {new_value}")