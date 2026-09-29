# While8. Дано N (> 0). Найти наибольшее K, для которого K*K <= N.
n = int(input())

k = 0

while (k + 1) * (k + 1) <= n:
 k += 1
 
print(k)