#String14 Дана строка. Подсчитать количество прописных латинских букв в ней

s = input()

count = 0

for ch in s:
    if "A" <= ch <= "Z":
        count += 1
print(count)