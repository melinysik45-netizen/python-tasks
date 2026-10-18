#Proc28. Описать функцию is_prime(n), возвращающую True, если n (> 1) простое, и False иначе. Найти
#количество простых в наборе из 10 чисел.

def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

count = 0
for i in range(10):
    k = int(input())
    if is_prime(k):
        count += 1
print(count)