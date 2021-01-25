import utils

from ecommerce.shipping import calc_shipping
import random


class Dice:
    def roll(self):
        return random.randint(1, 6), random.randint(1, 6)


dice = Dice()
for i in range(5):
    print(dice.roll())

print("hello")