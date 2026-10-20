#String5 Дано N (1 ≤ N ≤ 26). Вывести строку из N последних строчных латинских букв в обратном
#порядке, начиная с «z»

n = int(input())
res = ''
for i in range(n):
    res += chr(ord('z') - i)
print(res)