from enemy import *
from zombie import *
from kakai import *


def battle(e: Enemy):  # polymorphism is here because the battle method is having different forms
    e.talk()
    e.kick()


zombie = Zombie(2, 10)
kakai = Kakai(1, 40)

# polymorphism in action
battle(zombie)
battle(kakai)

# print(zombie.walk(), zombie.trouble())
