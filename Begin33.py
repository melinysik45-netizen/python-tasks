#Известно, что X кг конфет стоит A рублей. Определить, сколько стоит 1 кг и Y кг
#этих же конфет.
x =float(input())
a = float(input())
y = float(input())

price_kg = a / x
price_y = price_kg * y

print(price_kg)
print(price_y)