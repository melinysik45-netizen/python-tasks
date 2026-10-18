#Proc6. Описать функцию digit_count_sum(k), возвращающую количество цифр и сумму цифр целого
#положительного числа k. Найти обе величины для пяти данных чисел.

def digit_count_sum(k):
    count = 0
    total = 0
    while k > 0:
        total += k % 10
        count += 1
        k //= 10
    return count, total

for i in range(5):
    k = int(input())
    c, s = digit_count_sum(k)
    print(c)
    print(s)
