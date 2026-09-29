# While3. Даны положительные N и K. Только через + и -:
# найти частное от деления нацело и остаток.

n = int(input())
k = int(input())

quotient = 0
rest = n

while rest >= k:
 rest -= k
 quotient += 1

print(quotient)
print(rest)