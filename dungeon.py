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


def hero_hit(strike_n, damage, crit_damage):
    """Урон героя в ударе номер strike_n.

    Возвращает пару (hit, crit): урон и признак критического удара.
    Каждый третий удар — критический. Ничего не меняет.
    """
    if strike_n % 3 == 0:
        return crit_damage, True
    return damage, False


def fight(enemy, hero_health, bonus, damage, crit_damage):
    """Бой с enemy до гибели одного из них. Печатает строки раундов.

    bonus — надбавка к урону героя (0 без эликсира), damage и
    crit_damage — обычный и критический урон героя.
    Возвращает (rounds, won, hero_health, loot).
    """
    stats = enemy_stats[enemy]
    name = enemy_ru[enemy]
    enemy_hp = float(stats["hp"])
    rounds = []
    round_n = 0
    print(f"Ты спускаешься по лестнице. Из темноты появляется {name}!")
    while enemy_hp > 0 and hero_health > 0:
        round_n += 1
        hit, crit = hero_hit(round_n, damage, crit_damage)
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


if __name__ == "__main__":
    rounds, won, hp, loot = fight("skeleton", 100, 0, 20.5, 41.0)
    print(f"самотест: раундов {len(rounds)}, победа={won}, трофеи={loot}")


