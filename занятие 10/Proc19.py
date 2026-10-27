#Proc19. Описать функцию ring_s(r1, r2), находящую площадь кольца между окружностями радиусов r1 и r2
#(r1 > r2), пользуясь формулой круга S = 3.14·R2. Найти площади трёх колец.

def circle_s(r):
    return 3.14 * r * r
def ring_s(r1, r2):
    return circle_s(r1) - circle_s(r2)

for i in range(3):
    r1 = float(input())
    r2 = float(input())
    print(ring_s(r1, r2))