# enemy object
class Enemy:

    def __init__(self, type_of_enemy, health_point, attack_damage):
        print('this is parameter constructor')

        self.type_of_enemy = type_of_enemy
        self.health_point = health_point
        self.attack_damage = attack_damage
