from exceptions import LowLevelError

def heal_apply (health, heal):
    """3) исключение с обработчиком Exception, с finally"""
    try:
        if health + heal > 100:
            raise ValueError ("Здоровье превысило 100")
        return health + heal

    except Exception as e:
        print (f"Ошибка при лечении: {e}")
        return health
    finally:
        print ("Лечение завершено")

def calculate_experience(level, points):
    """5) функция с генерацией исключений"""
    try:
        if points < 0:
            raise ValueError("Очки опыта не могут быть отрицательными")
        if level < 1:
            raise LowLevelError("Уровень должен быть не менее 1")
        experience = level * points
        return experience      
    except ValueError as e:
        print(f"Ошибка опыта: {e}")
        return 0
    except LowLevelError as e:
        print(f"Ошибка уровня: {e}")
        return 0
    finally:
        print("Подсчет опыта завершен.")

