#Proc7 Функция invert_digits(k) возвращает число с обратным порядком цифр. Перевернуть пять
#данных чисел

def invert_digits(k):
    result = 0
    while k > 0:
        last_digit = k % 10
        result = result * 10 + last_digit
        k = k // 10
    return result
for i in range(5):
    k = int(input())
    print(invert_digits(k))
    
