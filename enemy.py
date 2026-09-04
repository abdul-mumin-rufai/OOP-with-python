# enemy object
class Enemy:
    type_of_enemy: str
    health_point: int = 100
    attack_damage: int = 2

    def kakai_talking(self):
        print(f'I am {self.type_of_enemy} i want with you')

    def kakai_fight(self):
        print(f'{self.type_of_enemy} attacks for damage of 2')

    def kakai_health_point(self):
        print(f'{self.type_of_enemy} has a {self.health_point} health points')
