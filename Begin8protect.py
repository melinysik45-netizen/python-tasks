#Begin8 protect
#Было: Даны два числа a и b. Найти их среднее
#арифметическое: (a + b)/2.
#Стало: То же, но при нечисловом вводе выводится
#«Ошибка ввода» вместо ответа; порядок и формула
#прежние

try:
    a = float(input())
    b = float(input())
    arithmetic_mean = (a + b) / 2
    print(arithmetic_mean)
except ValueError:
    print("Ошибка ввода")