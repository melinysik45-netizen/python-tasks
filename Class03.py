#Class3. Описать класс Counter со счётчиком, стартующим с нуля, и методами inc() и dec(); метод value()
#возвращает текущее значение. Прочитать три команды из слов «inc», «dec», «value» и выполнить их над
#одним счётчиком, печать только на «value».


class Counter:
    def __init__(self):
        self.total = 0
    def inc(self):
        self.total += 1
    def dec(self):
        self.total -= 1
    def value(self):
        return self.total
c = Counter()
for i in range(3):
    cmd = input()
    if cmd == "inc":
        c.inc()
    elif cmd == "dec":
        c.dec()
    else:
        print(c.value())