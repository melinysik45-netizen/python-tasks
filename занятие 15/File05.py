#File5. Дано имя файла целых чисел. Найти количество элементов файла. Если файла с таким именем не
#существует, вывести −1.

import os
name = input()
if not os.path.exists(name):
    print(-1)
else:
    with open(name, encoding="utf-8") as f:
        count = 0
        for line in f:
            if line.strip() != "":
                count += 1
    print(count)