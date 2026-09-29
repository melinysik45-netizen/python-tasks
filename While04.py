#While4 Дано целое число N (> 0). 
# Если оно является степенью числа 3, то вывести TRUE, если не является
#— вывести FALSE.

n = int(input())

rest = n

while rest > 1 and rest % 3 == 0:
    rest //= 3
print(rest == 1)