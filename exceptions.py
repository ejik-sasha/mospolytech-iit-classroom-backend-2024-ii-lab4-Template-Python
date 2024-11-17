class LowLevelError(Exception):
    """6.1) Пользовательское исключение"""
    def __init__(self, message="Уровень персонажа слишком низок!"):
        self.message = message
        super().__init__(self.message)


class InvalidSkillError(Exception): 
    """6.2) Пользовательское исключение"""
    def __init__(self, message="Неверный навык!"):
        self.message = message
        super().__init__(self.message)


class NegativeDamageError(Exception): 
    """6.3) Пользовательское исключение"""
    def __init__(self, message="Урон не может быть отрицательным!"):
        self.message = message
        super().__init__(self.message)

class LowManaError(Exception): 
    """6.4) Пользовательское исключение"""
    def __init__(self, message="Недостаточно маны!"):
        self.message = message
        super().__init__(self.message)

class InvalidArmorError(Exception):
    """6.5) Пользовательсоке исключение"""
    def __init__(self,message="Броня не может быть отрицательной"):
        self.message = message
        super().__init__(self.message)



def use_skill(character_level, skill_name, mana_cost, current_mana):
    """7) Пример использования пользовательских исключений"""
    try:
        if character_level < 5 and skill_name == "fireball":
            raise LowLevelError("Для использования огненного шара нужен уровень 5 и выше!")
        if current_mana < mana_cost:
            raise LowManaError()
        if skill_name not in ["fireball", "heal", "shield"]:
            raise InvalidSkillError()

        print(f"Навык '{skill_name}' использован успешно.")
        return True

    except LowManaError as e:
        print(f"Ошибка: {e}")
        return False
    except InvalidSkillError as e:
        print(f"Ошибка: {e}")
        return False
    except LowLevelError as e:
        print(f"Ошибка: {e}")
        return False

    finally:
        print("Попытка использования навыка завершена.")