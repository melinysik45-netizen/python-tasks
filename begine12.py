#Begin12 Даны катеты прямоугольного треугольника a и b. 
#Найти его гипотенузу c и периметр P: c = √(a2 + b2), P = a + b + c.

a = float(input())
b = float(input())

c = (a ** 2 + b ** 2) ** 0.5
perimeter = a + b + c

print(c)
print(perimeter)