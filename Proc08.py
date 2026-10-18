#Proc8 Функция add_right_digit(d, k) возвращает число k с приписанной справа цифрой d (0–9).
#Приписать к данному K справа D1 и D2, печатая результат каждого шага

def add_right_digit(d, k):
    result = k * 10 + d
    return result
k = int(input())
d1 = int(input())
d2 = int(input())
first_step_result = add_right_digit(d1, k)
print(first_step_result)
final_result = add_right_digit(d2, first_step_result)
print(final_result)
