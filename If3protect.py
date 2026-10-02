#If3 protect
#Было: Дано целое число. Положительное — прибавить 1,
#отрицательное — вычесть 2, нулевое — заменить на 10.
#Вывести результат.
#Стало То же, но при нечисловом вводе выводится
#«Ошибка ввода»; ветки if не меняются
try:
    number = int(input())
    if number > 0:
        number += 1
    elif number < 0:
        number -= 2
    else:
        number = 10
    print(number)
except ValueError:
    print("Ошибка ввода")