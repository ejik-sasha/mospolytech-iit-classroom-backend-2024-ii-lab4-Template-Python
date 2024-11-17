from exceptions import LowLevelError, NegativeDamageError, InvalidArmorError

def calculate_defense (level, armor):
    """1.2) возвращает исключение без обработки"""
    if level < 1:
        raise LowLevelError
    if armor < 0:
        raise InvalidArmorError
    return level * armor

def defend (defender_level, defender_armor, incoming_damage):
    """4.2) исключение с несколькими обработчиками"""
    try:
        defense = calculate_defense(defender_level, defender_armor)
        if incoming_damage - defense < 0:
            raise NegativeDamageError
        return incoming_damage - defense
    except LowLevelError as e:
        print(f"Ошибка защиты: {e}")
        return incoming_damage # Весь урон проходит
    except NegativeDamageError as e:
        print(f"Ошибка защиты: {e}")
        return 0 # Нет урона
    except InvalidArmorError as e:
        print(f"Ошибка защиты: {e}")
        return 0
    finally:
        print("Защита завершена.")

