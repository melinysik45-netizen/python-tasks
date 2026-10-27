#Proc30. Описать функцию digit_n(k, n), возвращающую n-ю цифру числа k справа налево; если цифр
#меньше n, вернуть -1. Для пяти данных чисел вызвать функцию с n от 1 до 5.

def digit_n(k, n):
    pos = 1
    cur = k
    while cur > 0:
        if pos == n:
            return cur % 10
        cur //= 10
        pos += 1
    return -1
for i in range(5):
    k = int(input())
    for n in range(1, 6):
        print(digit_n(k, n))