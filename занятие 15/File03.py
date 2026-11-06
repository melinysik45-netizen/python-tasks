#File3 Дано имя файла и вещественные A и D. Записать в файл 10 первых членов прогрессии A, A+D,
#A+2·D, ...

import os

name = input("Введите имя файла: ")
a = float(input("Введите начальный член A: "))
d = float(input("Введите разность прогрессии D: "))

with open(name, "w", encoding="utf-8") as f:
    for i in range(10):
        term = a + i * d
        f.write(str(term) + "\n")
