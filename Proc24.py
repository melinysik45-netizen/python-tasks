#Proc24 Функция even(k) возвращает True для чётного k. Найти количество чётных в наборе из 10
#чисел

def even(k):
    if k % 2 == 0:
        return True
    return False
count = 0
for i in range(10):
    k = int(input())
    if even(k):
        count += 1
print(count)