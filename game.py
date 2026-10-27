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
import random
enemies = ["Гуль", "Скелет", "Летучая мышь", "Паук"]
log = []
gold_total = 0
ability_bonus = 0

damage = 0
crit_damage = 0

# --- Функции --------------------------------------
def hero_hit(strike_n):
    """Урон героя в ударе номер strike_n.
    возвращает пару(hit, crit): урон и признак критического удара.
    читает глобальные damage и crit_damage, ничего не меняет """
    if strike_n % 3 == 0:
        return crit_damage, True
    return damage, False

def fight(enemy, hero_health, bonus=0):
    """Бой с enemy до гибели одного из них.
    bonus - надбавка к урону героя, по умолчанию = 0: без элексира бой идет как прежде
    надбавка прибавляется к удару после крита. печатает строки раундов.
    возвращает (rounds, won, hero_health, loot)"""
    enemy_hp = 45.0
    rounds = []
    round_n = 0
    print(f"Ты спускаешься по лестнице. Из темноты появляется {enemy}!")
    while enemy_hp > 0 and hero_health > 0:
        round_n += 1
        hit, crit = hero_hit(round_n)
        hit = hit + bonus
        enemy_hp -= hit
        line = f"Раунд {round_n}: герой наносит {hit:.1f}"
        if crit:
            line += " — критический удар!"
        else:
            line += "."
        if enemy_hp <= 0:
            line += " Враг падает."
            rounds.append([round_n, hit, 0])
        else:
            blow = random.randint(2, 6)
            hero_health -= blow
            line += f" Здоровье врага ({enemy}): {enemy_hp:.1f}. {enemy.capitalize()} бьёт на {blow}."
            rounds.append([round_n, hit, blow])
        print(line)
    won = enemy_hp <= 0
    if won:
        loot = 10 + 5 * round_n
    else:
        loot = 0
    return rounds, won, hero_health, loot

def buy(price, gold, quantity=1):
    """Покупает quantity штук товара ценой price за золото gold.

    quantity по умолчанию 1. Возвращает (gold_left, ok): остаток
    золота и признак успешной покупки. Ничего не печатает.
    """
    cost = price * quantity
    if gold >= cost:
        return gold - cost, True
    return gold, False

def print_leaderboard(log):
    """Печатает топ-3 раундов по урону героя и рекорд врага.

    Возвращает None: функция только печатает.
    """
    if not log:
        print("Ты ещё не сражался.")
        return
    top = sorted(log, key=lambda r: r[1], reverse=True)[:3]
    print("Таблица лидеров (урон героя):")
    for i in range(len(top)):
        print(f"{i + 1}. Раунд {top[i][0]}: {top[i][1]:.1f}")
    worst = max(log, key=lambda r: r[2])
    print(f"Самый сильный удар врага: {worst[2]} (раунд {worst[0]}).")

def print_run_summary(log):
    """Печатает итог забега: суммарный и средний урон героя.

    Возвращает None. Безопасна на пустом журнале.
    """
    total = sum(r[1] for r in log)
    rounds = len(log)
    if rounds > 0:
        print(f"Урон: {total:.1f} за {rounds} раундов, в среднем {total / rounds:.1f}.")
    else:
        print("В этом забеге боёв не было.")
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

# Потолки: с чем герой вошёл в подземелье
max_health = health
max_stamina = stamina
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

menu_last = 9
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
        print("7 - спуститься глубже")
        print("8 - таблица лидеров")
        print("9 - магазин")
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

            case "7":
                if not enemies:
                    print("Ты спускаешься по лестнице, но подземелье пусто.")
                else:
                    enemy = random.choice(enemies)
                    rounds, won, health, loot = fight(enemy, health, bonus=ability_bonus)
                    for r in rounds:
                        log.append(r)
                    if won:
                        gold_total += loot
                        enemies.remove(enemy)
                        print(f"Враг повержен: {enemy}! Врагов в подземелье осталось: {len(enemies)}. Трофеи: {loot} золота.")
                    print(f"Бой: {len(rounds)} раундов.")

            case "8":
                print_leaderboard(log)

            case "9":
                print("Магазин:")
                print("1 - зелье (+10 здоровья): 10 золота")
                print("2 - масло для факела (+5 сил): 15 золота")
                print("3 - боевой эликсир (+2 к урону до конца забега): 40 золота")
                print("Номер предмета (0 — ничего не покупать):")
                item = input()
                prices = (10, 15, 40)
                names = ("зелье", "масло для факела", "боевой эликсир")
                if item in ("1", "2", "3"):
                    price = prices[int(item) - 1]
                    name = names[int(item) - 1]
                    print("Количество (Enter — одна штука):")
                    qty_line = input()
                    ok = None
                    if qty_line == "":
                        qty = 1
                        gold_total, ok = buy(price, gold_total)
                    else:
                        try:
                            qty = int(qty_line)
                        except ValueError:
                            qty = 0
                        if qty < 1:
                            print("Количество должно быть целым числом от 1.")
                        else:
                            gold_total, ok = buy(price, gold_total, quantity=qty)
                    if ok:
                        if item == "1":
                            health = min(health + 10 * qty, max_health)
                        elif item == "2":
                            stamina = min(stamina + 5 * qty, max_stamina)
                        else:
                            ability_bonus += 2 * qty
                        print(f"Куплено: {qty} {name} за {price * qty} золота. Осталось золота: {gold_total}.")
                    elif ok is False:
                        print(f"Не хватает золота: нужно {price * qty}, есть {gold_total}.")
                elif item != "0":
                    print("Такого предмета в магазине нет.")
            
            case "0":
                print("Вы поднимаетесь обратно к свету. подземелье остается позади.")
                outcome = "Выход"
                running = False

            case _:
                print("Такого действия нет.")

        if running:
            actions += 1
        print()
        print(f"Здоровье: {health} Запас сил: {stamina} Врагов осталось: {len(enemies)} Золото: {gold_total}")
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
    print_run_summary(log)
