from enemy import *
from zombie import *
from kakai import *
from hero import *


def battle(e1: Enemy, e2: Enemy):  # polymorphism is here because the battle method is having different forms
    e1.talk()
    e2.talk()

    while e1.health_point > 0 and e2.health_point > 0:
        print('-------')
        e1.special_attack()
        e2.special_attack()
        print(f'{e1.get_type_of_enemy()}: {e1.health_point} HP left')
        print(f'{e2.get_type_of_enemy()}: {e2.health_point} HP left')
        e2.kick()
        e1.health_point -= e2.attack_damage
        e1.kick()
        e2.health_point -= e1.attack_damage

    print('-------------')
    if e1.health_point > 0:
        print(f'{e1.get_type_of_enemy()} wins!!!')
    else:
        print(f'{e2.get_type_of_enemy()} wins!!!')


def hero_battle(hero: Hero, enemy: Enemy):  # polymorphism is here because the battle method is having different forms

    while hero.health_point > 0 and enemy.health_point > 0:
        print('-------')

        print(f'Hero: {hero.health_point} HP left')
        print(f'{enemy.get_type_of_enemy()}: {enemy.health_point} HP left')
        enemy.kick()
        hero.health_point -= enemy.attack_damage
        hero.kick()
        enemy.health_point -= hero.attack_damage

    print('-------------')
    if hero.health_point > 0:
        print(f'Hero wins!!!')
    else:
        print(f'{enemy.get_type_of_enemy()} wins!!!')


zombie = Zombie(10, 3)
kakai = Kakai(10, 3)
my_hero = Hero(10, 3)
weapon = Weapon('Gun', 5)
my_hero.weapon = weapon  # composition here because the hero class contain another class weapon
my_hero.equip_weapon()

# polymorphism in action
hero_battle(my_hero, kakai)

# print(zombie.walk(), zombie.trouble())
