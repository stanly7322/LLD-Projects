
import random

class Dice:
    def __init__(self):
        print("Dice is created successfully with 6 sides each side has a value from 1 to 6")

    def roll(self):
        random_number = random.randint(1, 6)
        return random_number
