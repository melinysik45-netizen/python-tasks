#String3 Дан символ C. Вывести символы, предшествующий C в кодовой таблице и следующий за ним

c = input()
code = ord(c)
print(chr(code -1), chr(code +1))
