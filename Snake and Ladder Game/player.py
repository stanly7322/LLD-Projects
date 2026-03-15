# Class Player -> to define players who plays the game 
# Currently Name and Age are only attributes added(you can add according to your need like stats email ....)

class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.position = 0
        print("Player " + self.name + " created successfully")

    def set_position(self, position):
        self.position = position

    def get_position(self):
        return self.position