from utils import find_max
from ecommerce.shipping import calc_shipping
import random


class Dice:
    def roll(self):
        return random.randint(1, 6), random.randint(1, 6)


dice = Dice()
print(dice.roll())
