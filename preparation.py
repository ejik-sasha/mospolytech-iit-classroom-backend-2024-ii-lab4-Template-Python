from exceptions import LowLevelError, InvalidSkillError, LowManaError

def use_special_skills(level, skill_type, mana):
    """4.3) исключение с несколькими обработчиками"""
    try:
        if level < 10:
            raise LowLevelError("Для использования особого навыка нужен 10 уровень!")
        if skill_type not in ["fireball", "heal"]:
            raise InvalidSkillError("Неверный тип особого навыка!")
        if mana < 50:
            raise LowManaError()

        print(f"Использован особый навык: {skill_type}")
        return 100 # сила эффекта
        
    except LowLevelError as e:
        print(f"Ошибка навыка (уровень): {e}")
        return 0
    except InvalidSkillError as e:
        print(f"Ошибка навыка (тип): {e}")
        return 0
    except LowManaError as e:
        print(f"Ошибка навыка (мана): {e}")
        return 0
    finally:
        print("Попытка использования особого навыка завершена.")



def equip_item(character_level, item_level):
    """8.1) Дополнительные функции с исключениями"""
    try:
        if character_level < item_level:
            raise LowLevelError("Уровень персонажа слишком низок для этого предмета!")
        print("Предмет экипирован.")
    except LowLevelError as e:
        print(e)


def calculate_critical_hit(chance):
    """8.2) Дополнительные функции с исключениями"""
    if not 0 <= chance <= 100:
        raise ValueError("Шанс критического удара должен быть от 0 до 100.")
    if chance <= 10:
        return True
    else:
        return False


def calculate_dodge_chance(agility):
    """8.3) Дополнительные функции с исключениями"""
    if agility < 0:
        raise ValueError("Ловкость не может быть отрицательной.")