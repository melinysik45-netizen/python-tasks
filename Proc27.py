#Proc27 Функция is_power_n(k, n) возвращает True, если k (> 0) — степень n (> 1). Даны n и набор из 10
#чисел: найти количество степеней

def is_power_n(k, n):
    if k <= 0:
        return False
    while k % n == 0:
        k = k // n
    if k == 1:
        return True
    return False
n = int(input(f"Введите степень"))
count = 0
for i in range(10):
    k = int(input(f"Введите числа:"))
    if is_power_n(k, n):
        count += 1
print(f"Количество степеней {n}: {count}")