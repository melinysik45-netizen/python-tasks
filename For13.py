#Дано целое число N (> 0). Найти значение выражения 1.1 − 1.2 + 1.3 − ... (N
#слагаемых, знаки чередуются).

n = int(input())

total = 0.0
sign = 1.0

for i in range(1, n + 1):
    term = 1 + (i / 10)
    total += sign * term
    sign *= -1
print(total)