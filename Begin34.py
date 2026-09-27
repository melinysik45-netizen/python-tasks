#Известно, что X кг шоколадных конфет стоит A рублей, а Y кг ирисок стоит B
#рублей. Определить, сколько стоит 1 кг шоколадных конфет, 1 кг ирисок, а
#также во сколько раз шоколадные конфеты дороже ирисок.

x = float(input())
a =float(input())
y = float(input())
b = float(input())

price_chocolate = a / x
price_toffee = b / y
ratio = price_chocolate - price_toffee

print(price_chocolate)
print(price_toffee)
print(ratio)