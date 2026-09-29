# While11. Дано N (> 1). Вывести наименьшее K, при котором
# сумма 1 + 2 + ... + K >= N, и саму эту сумму.

n = int(input())
total = 0
k = 0

while total < n:
 k += 1
 total += k
 
print(k)
print(total)
