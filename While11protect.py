#While11 protect
#Дано N (> 1). Вывести наименьшее K, при котором
#сумма 1 + 2 + … + K ≥ N, и саму сумму.

#То же, но защищено чтение N: при нечисловом
#вводе выводится «Ошибка ввода»; цикл не меняется

try:
    n = int(input())
    total = 0
    k = 0
    while total < n:
        k += 1
        total += k
    print(k)
    print(total)
except ValueError:
    print("Ошибка ввода")