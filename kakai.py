from enemy import *
import random


class Kakai(Enemy):
    def __init__(self, health_point, attack_damage):
        super().__init__(type_of_enemy='Kakai',
                         health_point=health_point,
                         attack_damage=attack_damage
                         )

    def talk(self):
        print('Kakai is turning, turning around')

    def special_attack(self):
        is_special_attack = random.random() < 0.2
        if is_special_attack:
            self.attack_damage += 9
            print('Kakai get angry and increase attack damage by 9')
