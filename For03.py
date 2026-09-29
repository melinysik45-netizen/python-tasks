# For3. Даны A и B (A < B). Вывести в порядке убывания все целые числа
# между A и B (не включая A и B) и их количество.

a = int(input())
b = int(input())

count = 0
for i in range(b - 1, a, -1):
    print(i)
    count += 1
print(count)
