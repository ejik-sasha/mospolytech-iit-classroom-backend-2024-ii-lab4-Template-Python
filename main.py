from preparation import use_special_skills, equip_item, calculate_critical_hit, calculate_dodge_chance
from damage import calculate_damage, apply_damage, attack
from defense import calculate_defense, defend
from after_attack import heal_apply, calculate_experience

from exceptions import level_up

def run_battle_simulation():
    try:
        calculate_damage(5, 50)
        apply_damage(100, 30)

        calculate_defense(6, 20)
        heal_apply(50, 20)

        attack(10, 60, 8, 10)
        defend(7, 30, 50)
        use_special_skills(12, "fireball", 60)
        #use_special_skills(12, "heal", 40)

        calculate_experience(5, 100)

        level_up(5)

        equip_item(10, 5)
        calculate_critical_hit(50)
        calculate_dodge_chance(20)

        print("Симуляция боя завершена успешно.")



    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    run_battle_simulation()