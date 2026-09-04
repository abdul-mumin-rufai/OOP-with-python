# enemy object
class Enemy:
    type_of_enemy: str
    health_point: int = 100
    attack_damage: int = 2

    def __int__(self):
        pass
    # this is optional, and it is called automatically by python when the object instance is created

    def __init__(self):
        print(f'This is an optional contractor but i am still')
        # this is non parameter constructor
