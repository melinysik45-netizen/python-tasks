#Dict11. Даны N слов (строки, могут повторяться). Построить словарь-счётчик: ключ — слово, значение —
#сколько раз оно встретилось. Вывести каждое слово и его счёт в порядке первого появления.

n = int(input())
counts = {}
for i in range(n):
    word = input()
    counts[word] = counts.get(word, 0) + 1
for word, count in counts.items():
    print(f"{word}: {count}")