#Дано целое число N (> 0). Найти произведение 1.1 · 1.2 · 1.3 · ... (N
#сомножителей).

n = int(input())

total = 1.0

for i in range(1, n + 1):
    multiplier = 1 + (i / 10)
    total *= multiplier
print(total)