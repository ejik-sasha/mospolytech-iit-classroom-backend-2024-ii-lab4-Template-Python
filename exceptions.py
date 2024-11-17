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

def level_up(level): 
    """7) Пример использования пользовательских исключений"""
    if level < 1:
        raise LowLevelError

    if level > 100:
        raise ValueError("Максимальный уровень 100!")
    return level + 1
