from enemy import *


class Kakai(Enemy):
    def __init__(self, health_point, attack_damage):
        super().__init__(type_of_enemy='Kakai',
                         health_point=health_point,
                         attack_damage=attack_damage
                         )
