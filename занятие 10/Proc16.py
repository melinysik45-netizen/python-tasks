#Proc16. Описать функцию sign(x), возвращающую -1 при x < 0, 0 при x = 0 и 1 при x > 0. Найти значение
#выражения Sign(A) + Sign(B) для данных A и B.

def sign(x):
    if x < 0:
        return -1
    if x == 0:
        return 0
    return 1

a = float(input())
b = float(input())
print(sign(a) + sign(b))