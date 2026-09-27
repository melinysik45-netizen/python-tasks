# If3. Если число положительное — прибавить 1; если отрицательное —
# вычесть 2; если нулевое — заменить на 10.
number = int(input())

if number > 0:
    number += 1
elif number < 0:
    number -= 2
else:
    number = 10

print(number)