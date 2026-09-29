# For7. Даны A и B (A < B). Найти сумму всех целых чисел от A до B включи

a = int(input())
b = int(input())

total = 0
for i in range(a, b + 1):
     total += i
print(total)