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

class Hero:
    """Герой забега: характеристики, текущее состояние и правила их изменения."""

    def __init__(self, name, health, strength, agility, luck):
        """Создаёт героя; урон и запас сил считаются от характеристик."""
        self.name = name
        self.health = health
        self.max_health = health
        self.strength = strength
        self.agility = agility
        self.luck = luck
        self.damage = 10 + strength * 1.5
        self.crit_damage = self.damage * 2
        self.stamina = health // 10 * luck
        self.max_stamina = self.stamina

    def __str__(self):
        """Формуляр героя одной строкой: print(hero) печатает её."""
        return (f"{self.name}: здоровье {self.health}, "
                f"урон {self.damage:.1f}, запас сил {self.stamina}")

    def strike(self, n):
        """Урон героя в ударе номер n: пара (hit, crit), каждый третий — крит."""
        if n % 3 == 0:
            return self.crit_damage, True
        return self.damage, False

    def spend_stamina(self, cost):
        """Тратит силы на шаг. Если сил не хватает, остаток списывается
        из здоровья. Возвращает True, если герой шёл «на упорстве»."""
        if self.stamina >= cost:
            self.stamina -= cost
            return False
        self.health -= cost - self.stamina
        self.stamina = 0
        return True

    def try_spend(self, cost):
        """Тратит cost сил, только если их хватает. Возвращает True/False."""
        if self.stamina >= cost:
            self.stamina -= cost
            return True
        return False

    def rest(self, amount):
        """Отдых: прибавляет силы без потолка (как в прежних этапах)."""
        self.stamina += amount

    def refuel(self, amount):
        """Масло для факела: прибавляет силы, но не выше потолка."""
        self.stamina = min(self.stamina + amount, self.max_stamina)

    def heal(self, amount):
        """Лечение: прибавляет здоровье, но не выше потолка."""
        self.health = min(self.health + amount, self.max_health)

    def hurt(self, dmg):
        """Получение урона. Возвращает None."""
        self.health -= dmg

    def to_dict(self):
        """Словарь состояния героя для JSON."""
        return {"name": self.name, "health": self.health,
                "max_health": self.max_health, "stamina": self.stamina,
                "strength": self.strength, "agility": self.agility,
                "luck": self.luck}

    @staticmethod
    def from_dict(data):
        """Создаёт героя из словаря сохранения.

        Конструктор получает максимум здоровья, чтобы пересчитать урон и
        потолок сил, а текущие здоровье и силы доводятся до файловых.
        """
        hero = Hero(data["name"], data["max_health"], data["strength"],
                    data["agility"], data["luck"])
        hero.health = data["health"]
        hero.stamina = data["stamina"]
        return hero

class Enemy:
    """Враг: рабочая копия карточки из enemy_stats на один бой."""

    def __init__(self, name, stats):
        """Создаёт врага по ключу name и карточке stats."""
        self.name = name
        self.title = enemy_ru[name]
        self.hp = float(stats["hp"])
        self.damage = stats["damage"]
        self.loot = stats["loot"]

def hero_hit(strike_n, damage, crit_damage):
    """Урон героя в ударе номер strike_n.

    Возвращает пару (hit, crit): урон и признак критического удара.
    Каждый третий удар — критический. Ничего не меняет.
    """
    if strike_n % 3 == 0:
        return crit_damage, True
    return damage, False


def fight(enemy, hero, bonus=0):
    """Бой героя с врагом до гибели одного из них. Печатает строки раундов.

    bonus — надбавка к урону героя (0 без эликсира).
    Здоровье героя меняется на месте. Возвращает (rounds, won, loot).
    """
    rounds = []
    round_n = 0
    name = enemy.title
    print(f"Ты спускаешься по лестнице. Из темноты появляется {name}!")
    while enemy.hp > 0 and hero.health > 0:
        round_n += 1
        hit, crit = hero.strike(round_n)
        hit = hit + bonus
        enemy.hp -= hit
        line = f"Раунд {round_n}: герой наносит {hit:.1f}"
        if crit:
            line += " — критический удар!"
        else:
            line += "."
        if enemy.hp <= 0:
            line += " Враг падает."
            rounds.append([round_n, hit, 0])
        else:
            hero.hurt(enemy.damage)
            line += (f" Здоровье врага ({name}): {enemy.hp:.1f}. "
                     f"{name.capitalize()} бьёт на {enemy.damage}.")
            rounds.append([round_n, hit, enemy.damage])
        print(line)
    won = enemy.hp <= 0
    loot = enemy.loot if won else 0
    return rounds, won, loot


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


