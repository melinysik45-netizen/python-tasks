#Proc9 Функция add_left_digit(d, k) возвращает число k с приписанной слева цифрой d (1–9).
#Приписать к данному K слева D1 и D2, печатая каждый шаг

def add_left_digit(d, k):
    multiplier = 1
    temp_k = k
    while temp_k > 0:
        temp_k = temp_k // 10
        multiplier = multiplier * 10
    return d * multiplier + k
k = int(input())
d1 = int(input())
d2 = int(input())
first = add_left_digit(d1, k)
print(first)
second = add_left_digit(d2, first)
print(second)
