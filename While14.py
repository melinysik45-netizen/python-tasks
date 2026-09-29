#While14 Дано число A (> 1). Вывести наибольшее из целых чисел K, для которых сумма 1 + 1/2 + … + 1/K
#будет меньше A, и саму эту сумму

a = float(input())

total = 0.0
k = 0

while total + (1 / (k + 1)) < a:
    k += 1
    total += 1 / k

print(k)
print(total)