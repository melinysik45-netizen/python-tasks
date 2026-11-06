#File10. Дан файл целых чисел. Создать новый файл, содержащий те же элементы, что и исходный файл,
#но в обратном порядке.
src = input()
dst = input()
with open(src, encoding="utf-8") as f:
    nums = [int(line) for line in f if line.strip()]
with open(dst, "w", encoding="utf-8") as f:
    for x in nums[::-1]:
        f.write(str(x) + "\n")