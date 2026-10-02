# Err1. Прочитать целое число и вывести его.
# Если введено не число — вывести "Ошибка ввода".
try:
    number = int(input())
    print(number)
except ValueError:
    print("Ошибка ввода")