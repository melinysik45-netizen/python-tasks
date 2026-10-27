#Proc26 Функция is_power5(k) возвращает True, если k (> 0) — степень пятёрки. Найти количество таких
#в наборе из 10 чисел

def is_power5(k):
    if k <= 0:
        return False
    while k % 5 == 0:
        k = k // 5
    if k == 1:
        return True
    return False
count = 0
for i in range(10):
    k = int(input())
    if is_power5(k):
        count += 1
print(f"Количество степеней 5: {count}")