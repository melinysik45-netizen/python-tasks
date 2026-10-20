#String4 Дано N (1 ≤ N ≤ 26). Вывести строку из N первых заглавных латинских букв

n = int(input())
res = ''
for i in range(n):
    res += chr(ord('A') + i)
print(res)