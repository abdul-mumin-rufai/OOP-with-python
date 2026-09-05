from enemy import *


class Zombie(Enemy):
    def __init__(self, health_point, attack_damage):
        super().__init__(  # inheriting from the parent class Enemy
            type_of_enemy='Zombie',
            health_point=health_point,
            attack_damage=attack_damage
        )

    def walk(self):
        print(f'Zombie is smuggling around')

    def trouble(self):
        print(f'me')
