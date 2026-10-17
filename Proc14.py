#Proc14 Функция shift_right3(a, b, c) возвращает тройку после правого циклического сдвига: a
#переходит на место b, b — на место c, c — на место a. Сдвинуть два набора

def shift_right3(a, b, c):
    return c, a, b

a1 =float(input())
b1 =float(input())
c1 =float(input())
a2 =float(input())
b2 =float(input())
c2 =float(input())

print(shift_right3(a1, b1, c1))
print(shift_right3(a2, b2, c2))