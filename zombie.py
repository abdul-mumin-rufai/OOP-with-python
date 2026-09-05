from enemy import *
import random


class Zombie(Enemy):
    def __init__(self, health_point, attack_damage):
        super().__init__(  # inheriting from the parent class Enemy
            type_of_enemy='Zombie',
            health_point=health_point,
            attack_damage=attack_damage
        )

    def walk(self):
        print(f'Zombie is smuggling around')

    def special_attack(self):
        is_special_attack = random.random() < 0.5
        if is_special_attack:
            self.health_point += 4
            print('Zombie regenerated HP of 4')

    def trouble(self):
        print(f'Zombie is spreading diseases')
