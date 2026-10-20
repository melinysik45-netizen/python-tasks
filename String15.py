#String15 Дана строка. Подсчитать общее количество строчных латинских и русских букв в ней

s = input()

count = 0
alphabet = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'

for ch in s:
    if ch in alphabet:
        count += 1
print(count)