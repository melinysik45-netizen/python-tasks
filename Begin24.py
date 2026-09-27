#Даны переменные A, B, C. Изменить их значения, переместив содержимое A в C,
#C — в B, B — в A, и вывести новые значения переменных A, B, C.
A = float(input())
B = float(input())
C = float(input())

temp = A
A = C
C = B
B = temp

print(A)
print(B)
print(C)