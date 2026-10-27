#Proc29 Функция digit_count(k) возвращает количество цифр k (> 0). Найти количество цифр пяти чисел

def digit_count(k):
    count_digits = 0
    while k > 0:
        k = k // 10
        count_digits += 1
    return count_digits
for i in range(5):
    k = int(input())
    print(digit_count(k))