#File6. Дано целое K и файл целых чисел. Вывести K-й элемент файла (элементы нумеруются с 1). Если
#такой элемент отсутствует, вывести −1.
k = int(input())
name = input()
with open(name, encoding="utf-8") as f:
    nums = [int(line) for line in f if line.strip()]
if 1 <= k <= len(nums):
    print(nums[k - 1])
else:
    print(-1)