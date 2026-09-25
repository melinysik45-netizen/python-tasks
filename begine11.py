#Begine11 Даны два ненулевых числа. 
#Найти сумму, разность, произведение и частное их модулей.

a = float(input())
b = float(input())

sum = abs(a) + abs(b)
difference = abs(a) - abs(b)
product = abs(a) * abs(b)
quotient = abs(a) / abs(b)

print(sum)
print(difference)
print(product)
print(quotient)