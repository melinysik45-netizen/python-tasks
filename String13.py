#String13. Дана строка. Подсчитать количество содержащихся в ней цифр.

s = input()
count = 0
for ch in s:
    if ch.isdigit():
        count += 1
print(count)