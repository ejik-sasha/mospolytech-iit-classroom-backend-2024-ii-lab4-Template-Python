from defense import calculate_defense
from exceptions import LowLevelError, InvalidSkillError, NegativeDamageError

def calculate_damage (level, skill):
    """1.1) возвращает исключение без обработки"""
    if level < 1:
        raise LowLevelError

    if skill < 0 or skill > 10:
        raise InvalidSkillError

    return level * skill

def apply_damage (damage, health):
    """2) исключение с обработчиком Exception, без finally"""
    try:
        if damage < 0:
            raise NegativeDamageError
        return health - damage
    except Exception as e:
        print(f"Ошибка при нанесении урона: {e}")
        return health

def attack (attacker_level, attacker_skill, defender_level, defender_armor):
    """4.1) исключение с несколькими обработчиками"""
    try:
        damage = calculate_damage(attacker_level, attacker_skill)
        defense = calculate_defense(defender_level, defender_armor)
        if damage - defense < 0:
            raise NegativeDamageError

    except LowLevelError as e:
        print(f"Ошибка атаки: {e}")
        return 0
    except InvalidSkillError as e:
        print(f"Ошибка атаки: {e}")
        return 0
    except NegativeDamageError as e:
        print (f"Ошибка защиты: {e}")
        return 0
    finally:
        print("Атака завершена")