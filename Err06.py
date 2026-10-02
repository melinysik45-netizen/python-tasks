#Err6 Та же задача, что Err5, но с двумя ветками: нечисловой индекс — «Ошибка ввода», индекс вне
#границ — «Нет такого символа».

try:
    text = input()
    number = int(input())
    print(text[number])
except IndexError:
    print("Нет такого символа")
except ValueError:
    print("Ошибка ввода")