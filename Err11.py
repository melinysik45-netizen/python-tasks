#Err11 Прочитать два числа и вывести их частное. Обе возможные ошибки обработать одним кортежем в
#except с сообщением «Посчитать не удалось»; при успехе в else вывести частное с двумя знаками
#после точки.

try:
    num1 = float(input())
    num2 = float(input())
    dev = num1 / num2
except(ValueError, ZeroDivisionError):
    print("Посчитать не удалось")
else:
    print(f"{dev:.2f}")