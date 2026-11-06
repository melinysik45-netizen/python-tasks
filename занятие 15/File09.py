#File9 Даны имена двух файлов: один существует и непуст (не обязательно первый), другой
#отсутствует. Создать отсутствующий и записать в него конечный и начальный элементы
#существующего

import os

file_a = input("Введите первое имя файла: ")
file_b = input("Введите второе имя файла: ")

if os.path.exists(file_a):
    src = file_a
    dst = file_b
else:
    src = file_b
    dst = file_a

with open(src, "r", encoding="utf-8") as f:
    nums = [line.strip() for line in f if line.strip()]

with open(dst, "w", encoding="utf-8") as f:
    f.write(nums[-1] + "\n")
    f.write(nums[0] + "\n")
