#Даны переменные A, B, C. Изменить их значения, переместив содержимое A в B,
#B — в C, C — в A, и вывести новые значения переменных A, B, C.

A = float(input())
B = float(input())
C = float(input())

temp = A

A = B
B = C
C = temp

print(A)
print(B)
print(C)