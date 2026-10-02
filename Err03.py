# Err3. Прочитать два целых числа и вывести частное.
# Нечисловой ввод — "Ошибка ввода", ноль в делителе —
# "Делить на ноль нельзя".
try:
    a = int(input())
    b = int(input())
    print(a / b)
except ValueError:
    print("Ошибка ввода")
except ZeroDivisionError:
    print("Делить на ноль нельзя")