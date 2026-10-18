#Proc22. Описать функцию calc(a, b, op), выполняющую над ненулевыми a и b операцию по целому op: 1 —
#вычитание, 2 — умножение, 3 — деление, остальные значения — сложение. Выполнить для данных A и B
#операции N1, N2, N3.

def calc(a, b, op):
    if op == 1:
        return a - b
    if op == 2:
        return a * b
    if op == 3:
        return a / b
    return a + b

a = float(input())
b = float(input())
n1 = int(input())
n2 = int(input())
n3 = int(input())

print(calc(a, b, n1))
print(calc(a, b, n2))
print(calc(a, b, n3))