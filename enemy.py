# enemy object
class Enemy:

    def __init__(self, type_of_enemy, health_point, attack_damage):
        self.__type_of_enemy = type_of_enemy  # this is a private attribute
        self.health_point = health_point
        self.attack_damage = attack_damage

    def talk(self):
        print(f'I am a {self.__type_of_enemy} i want to fight with you')

    def walk(self):
        print(f'{self.__type_of_enemy} walk towards you')

    def kick(self):
        print(
            f'{self.__type_of_enemy} has health point of {self.health_point} and kicks you to cause '
            f'{self.attack_damage} damage')

    def special_attack(self):
        print(f'There is no special attack')

    # we use the get method to access a private attribute
    def get_type_of_enemy(self):
        return self.__type_of_enemy
