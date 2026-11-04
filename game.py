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

prices = {"potion": 10, "torch_oil": 15, "war_elixir": 40}

enemy_stats = {
    "skeleton": {"hp": 45, "damage": 6, "loot": 25},
    "ghoul": {"hp": 30, "damage": 4, "loot": 15},
    "spider": {"hp": 20, "damage": 3, "loot": 10},
    "bat": {"hp": 12, "damage": 2, "loot": 5},
}

enemy_ru = {
    "skeleton": "скелет",
    "ghoul": "гуль",
    "spider": "паук",
    "bat": "летучая мышь",
}

enemies = ["ghoul", "skeleton", "spider", "bat"]
log = []
inventory = {} 
gold_total = 0
ability_bonus = 0

damage = 0
crit_damage = 0

# Словарь-переводчик: номер пункта меню
num_to_verb = {"1": "look", "2": "go", "3": "rest", "4": "listen",
               "5": "torch", "6": "train", "7": "descend", "8": "leaders",
               "9": "shop", "10": "backpack", "11": "drink", "0": "exit"}

# Список команд для справки help
commands = ["look", "go", "rest", "listen", "torch", "train", "descend",
            "leaders", "shop", "backpack", "drink potion",
            "buy <предмет> [количество]", "exit"]

# Строки меню: печатаются одним join
MENU = ["Что делаешь? (номер или команда; help — справка)",
        "1 - осмотреться (look)",
        "2 - идти вперёд (go)",
        "3 - отдохнуть (rest)",
        "4 - прислушаться (listen)",
        "5 - зажечь факел (torch)",
        "6 - тренировка (train)",
        "7 - спуститься глубже (descend)",
        "8 - таблица лидеров (leaders)",
        "9 - магазин (shop)",
        "10 - рюкзак (backpack)",
        "11 - выпить зелье (drink)",
        "0 - выйти из подземелья (exit)"]

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
    stats = enemy_stats[enemy]
    name = enemy_ru[enemy]
    enemy_hp = float(stats["hp"])
    rounds = []
    round_n = 0
    print(f"Ты спускаешься по лестнице. Из темноты появляется {name}!")
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
            blow = stats["damage"]
            hero_health -= blow
            line += (f" Здоровье врага ({name}): {enemy_hp:.1f}. "
                     f"{name.capitalize()} бьёт на {blow}.")
            rounds.append([round_n, hit, blow])
        print(line)
    won = enemy_hp <= 0
    loot = stats["loot"] if won else 0
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

def print_backpack_left(inventory):
    """Печатает, что осталось в рюкзаке при прощании. Возвращает None."""
    if inventory:
        print("В рюкзаке осталось:")
        for name, qty in inventory.items():
            print(f"{name}: {qty} шт.")
    else:
        print("В рюкзаке осталось: ничего.")

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

# --- Главный цикл игры ---------------------------------
running = True
actions = 0
outcome = "Прерывание" 
try:
    while running:
        print("\n".join(MENU))
        print()

        # 1. нормализация: убрать поля и регистр
        line = input()
        cmd = line.strip().lower()
        while cmd == "":
            print("Пустая команда. Введи команду или номер.")
            line = input()
            cmd = line.strip().lower()

        # 2. резка на слова (номер переводим в слово)
        words = cmd.split()
        verb = words[0]
        if cmd in num_to_verb:
            verb = num_to_verb[cmd]
        
        match verb:
            case "look":
                print("Ты осматриваешься. Вокруг ряды старых захоронений, дальний конец теряется во тьме.")

            case "go":
                cost = 2
                if stamina >= cost:
                    stamina -= cost
                    print("Ты осторожно идёшь вперёд по узкому проходу между костницами.")
                else:
                    health -= cost - stamina
                    stamina = 0
                    print("Сил больше нет — ты идёшь на одном упорстве.")

            case "rest":
                restore = 5
                stamina += restore
                print("Ты садишься у стены и переводишь дух. Силы возвращаются.")

            case "listen":
                print("Ты замираешь и слушаешь. Где-то в темноте осыпается земля.")

            case "torch":
                cost = 3
                if stamina >= cost:
                    stamina -= cost
                    print("Ты зажигаешь факел. Стены катакомб оживают неровным светом, полки с костями отбрасывают тени.")
                else:
                    print("Сил недостаточно, чтобы даже высечь искру.")

            case "train":
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
                        hit_damage, crit = hero_hit(i)
                        if crit:
                            crit_count += 1
                            print(f"Удар {i}: {hit_damage:.1f} — критический!")
                        else:
                            print(f"Удар {i}: {hit_damage:.1f}")
                        total_damage += hit_damage

            case "descend":
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
                        print(f"Враг повержен: {enemy_ru[enemy]}! Врагов в подземелье осталось: {len(enemies)}. Трофеи: {loot} золота.")
                    print(f"Бой: {len(rounds)} раундов.")

            case "leaders":
                print_leaderboard(log)

            case "shop":
                print("Магазин:")
                for name, price in prices.items():
                    print(f"{name}: {price} золота")
                print("Чтобы купить: buy <предмет> [количество].")

            case "buy":
                if len(words) > 1 and words[-1].isdigit():
                    qty = int(words[-1])
                    item = "_".join(words[1:-1])
                else:
                    qty = 1
                    item = "_".join(words[1:])
                if item == "":
                    print("Что купить? Напиши: buy <предмет> [количество].")
                    continue
                if item not in prices:
                    print("Такого предмета в магазине нет.")
                    continue
                if qty < 1:
                    print("Количество должно быть целым числом от 1.")
                    continue
                price = prices[item]
                gold_total, ok = buy(price, gold_total, quantity=qty)
                if ok:
                    if item == "torch_oil":
                        stamina = min(stamina + 5 * qty, max_stamina)
                    elif item == "war_elixir":
                        ability_bonus += 2 * qty
                    inventory[item] = inventory.get(item, 0) + qty
                    print(f"Куплено: {qty} {item} за {price * qty} золота. Осталось золота: {gold_total}.")
                else:
                    print(f"Не хватает золота: нужно {price * qty}, есть {gold_total}.")

            case "backpack":
                if not inventory:
                    print("Рюкзак пуст.")
                else:
                    print("Рюкзак:")
                    for name, qty in inventory.items():
                        print(f"{name}: {qty} шт.")

            case "drink":
                item = "_".join(words[1:]) or "potion"
                if item != "potion":
                    print(f"«{item}» выпить нельзя.")
                    continue
                if inventory.get("potion", 0) == 0:
                    print("В рюкзаке нет зелий.")
                else:
                    health = min(health + 10, max_health)
                    inventory["potion"] -= 1
                    if inventory["potion"] == 0:
                        del inventory["potion"]
                    print(f"Ты пьёшь зелье. Здоровье: {health}. Зелий осталось: {inventory.get('potion', 0)}.")

            case "help":
                print("Команды: " + ", ".join(commands) + ".")
                print("Номера 0-11 работают как раньше.")

            case "exit":
                print("Вы поднимаетесь обратно к свету. подземелье остается позади.")
                outcome = "Выход"
                running = False

            case _:
                print(f"Не понимаю команду: '{line.strip()}'. Введи 'help'.")
                continue

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
    print_backpack_left(inventory)
    print(frame)
    if outcome == "Гибель":
        print(f"Ты не дошел, {hero_name}. Действий совершено: {actions}")
    elif outcome == "Выход":
        print(f"Забег окончен, {hero_name}. Действий совершено: {actions}.")
    else:
        print(f"Сеанс прерван, {hero_name}. Действий совершено: {actions}.")
    print_run_summary(log)
