from weapon import *


class Hero:
    def __init__(self, health_point, attack_damage):
        self.health_point = health_point
        self.attack_damage = attack_damage
        self.is_weapon_equipped = False
        self.weapon: Weapon = None  # composition here because the hero class contain another class weapon

    def equip_weapon(self):
        if self.weapon is not None and not self.is_weapon_equipped:
            self.attack_damage += self.weapon.attack_increase
            self.is_weapon_equipped = True

    def kick(self):
        print(f'Hero kick to cause {self.attack_damage} damage')
