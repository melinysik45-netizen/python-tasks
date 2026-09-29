# While15. Вклад 1000 руб. растёт на P процентов в месяц.
# Найти, через сколько месяцев он превысит 1100 руб.

p = float(input())
deposit = 1000.0
months = 0

while deposit <= 1100:
 deposit = deposit * (1 + p / 100)
 months += 1
 
print(months)
print(deposit)