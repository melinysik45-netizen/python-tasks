# Integer5. Даны A и B (A > B). На отрезке A размещены отрезки длины B.
# Найти длину незанятой части отрезка A.
segment = int(input())
piece = int(input())
free_part = segment % piece
print(free_part)