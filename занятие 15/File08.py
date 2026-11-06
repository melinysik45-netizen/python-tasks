#File8 Даны имена двух файлов: первый существует и непуст, второй отсутствует. Создать второй и
#записать в него первый и последний элементы первого

import os

src = input("Введите имя существующего файла: ")
dst = input("Введите имя нового файла: ")

with open(src, "r", encoding="utf-8") as f:
    nums = [line.strip() for line in f if line.strip()]

first_elem = nums[0]
last_elem = nums[-1]

with open(dst, "w", encoding="utf-8") as f:
    f.write(first_elem + "\n")
    f.write(last_elem + "\n")
