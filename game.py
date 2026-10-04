# ================================================
# ИГРА «ТЁМНЫЕ КАТАКОМБЫ»
# Автор: Ганиева Мелина
# Дата: 25.09.26
#
# Пункт 4 — «прислушаться»: герой замирает
# и слушает, что происходит в темноте. Пока
# пункт только выводится в меню — обрабатывать
# его будем на третьем занятии.
#
# Пункт 5 — «зажечь факел»: герой достаёт и зажигает факел,
# чтобы осветить путь. Пока тоже только пункт меню.
# ================================================

# --- Заголовок ------------------------------------
title = "ТЁМНЫЕ КАТАКОМБЫ"
frame = "=" * 22

print(frame)
print(" " + title + " ")
print(frame)
print()
# --- Знакомство с героем --------------------------
print("Как зовут героя?")
hero_name = input()

print(f"Добро пожаловать, {hero_name}!")
print("Ты спускаешься в катакомбы. Стены пахнут сыростью, а в темноте гулко отдаются твои шаги.")
print()

# --- Настройка героя -------------------------------
print("Настройка героя.")
print("Здоровье, сила, ловкость, удача — по одному числу в строке:")
while True:
    try:
        health = int(input())
        strength = int(input())
        agility = int(input())
        luck = int(input())
        if health <= 0:
            raise ValueError(f"Здоровье должно быть положительным, а ты ввел {health}")
        if strength < 0 or agility < 0 or luck < 0:
            raise ValueError("Характеристики должны быть положительными")
        break
    except ValueError as e:
        print(f"{e}. Должны быть только числа. Попробуй еще раз все четыре:")

# --- Расчёт урона ----------------------------------
base_attack = 10
damage = base_attack + strength * 1.5
crit_damage = damage * 2
stamina = health // 10 * luck

# --- Формуляр героя --------------------------------
print("Характеристики героя:")
print(f"Здоровье: {health}")
print(f"Сила: {strength}")
print(f"Ловкость: {agility}")
print(f"Удача: {luck}")
print()
print(f"Урон героя: {damage:.1f}")
print(f"Критический урон: {crit_damage:.1f}")
print(f"Запас сил: {stamina}")
print()

menu_last = 6
# --- Главный цикл игры ---------------------------------
running = True
actions = 0
outcome = "Прерывание" 
try:
    while running:
        print("Что делаешь?")
        print("1 - осмотреться")
        print("2 - идти вперёд")
        print("3 - отдохнуть")
        print("4 - прислушаться")
        print("5 - зажечь факел")
        print("6 - тренировка")
        print("0 - выйти из подземелья")
# --- Выбор действия --------------------------------
    while True:
        choice = input()
        try:
            menu_number = int(choice)
        except ValueError:
            print("Такого пункта нет. Введи номер пункта из меню.")
            continue
        if 0 <= menu_number <= menu_last:
            break
        print("Такого пункта нет. Введи номер пункта из меню.")

    match choice:
        case "1":
            print("Ты осматриваешься. Вокруг ряды старых захоронений, дальний конец теряется во тьме.")

        case "2":
            cost = 2
            if stamina >= cost:
                stamina -= cost
                print("Ты осторожно идёшь вперёд по узкому проходу между костницами.")
            else:
                health -= cost - stamina
                stamina = 0
                print("Сил больше нет — ты идёшь на одном упорстве.")

        case "3":
            restore = 5
            stamina += restore
            print("Ты садишься у стены и переводишь дух. Силы возвращаются.")  

        case "4":
         print("Ты замираешь и слушаешь. Где-то в темноте осыпается земля.")

        case "5":
            cost = 3
            if stamina >= cost:
                stamina -= cost
                print("Ты зажигаешь факел. Стены катакомб оживают неровным светом, полки с костями отбрасывают тени.")
            else:
                print("Сил недостаточно, чтобы даже высечь искру.")

        case "6":
            cost = 4
            if stamina < 4:
                print("Ты очень устал для тренировки")
            else:
                stamina -= cost
                strikes = 6
                total_damage = 0
                crit_count = 0
                print("Ты подходишь к тренировочному чучелу из старых досок.")
                print("Оно стояло тут с тех пор, как сюда кто-то спускался")
                print()
                print(f"Наносите {strikes} ударов.")
                
                for i in range(1, strikes + 1):
                    if i % 3 == 0:
                        hit_damage = crit_damage
                    else:
                        hit_damage = damage
                    if i % 3 == 0:
                        print(f"Удар {i}: {hit_damage:.1f} — критический!")
                    else:
                        print(f"Удар {i}: {hit_damage:.1f}")
                    total_damage += hit_damage
                    if i % 3 == 0:
                        crit_count += 1
                for i in range(1, strikes + 1):
                    print(f"Удар {i}: {damage:.1f} урона")
        
        case "0":
            print("Вы поднимаетесь обратно к свету. подземелье остается позади.")
            running = False

        case _:
            print("Такого действия нет.")

    if running:
        actions += 1
    print()
    print(f"Здоровье: {health} Запас сил: {stamina}")
    print()

    if health <= 0:
        print(f"{hero_name} падает без сил. Подземелье не щадит никого.")
        outcome = "Гибель"
        running = False
except KeyboardInterrupt:
    print()
    print("Игрок прервал сеанс")
# --- Прощание --------------------------------------
finally:
    print(frame)
    if outcome == "Гибель":
        print(f"Ты не дошел, {hero_name}. Действий совершено: {actions}")
    elif outcome == "Выход":
        print(f"Забег окончен, {hero_name}. Действий совершено: {actions}.")
    else:
        print(f"Сеанс прерван, {hero_name}. Действий совершено: {actions}.")
    print(frame)