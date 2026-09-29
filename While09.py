#While9 Дано целое число N (> 1). Найти наименьшее целое число K, при котором выполняется
#неравенство 3^K > N.

n = int(input())

power = 0
k = 0

while power <= n:
    power *= 3
    k += 1

print(k)