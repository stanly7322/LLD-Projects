# Elevator will start from ground floor

from direction import Direction

class Elevator:
    def __init__(self, id, floors):
        self.__id = id
        self.__floors = floors
        self.__current_floor = 0
        self.__direction = None

    def get_floors(self):
        return self.__floors

    def get_id(self):
        return self.__id
    
    def get_current_floor(self):
        return self.__current_floor
    
    def get_direction(self):
        return self.__direction
    
    def set_direction(self, direction):
        self.__direction = direction

    def move_one_floor(self, direction):
        print(f"Elevator {self.__id} is in floor {self.__current_floor}")
        self.__direction = direction

        if direction == Direction.UP:
            print(f"Elevator {self.__id} is moving up to floor {self.__current_floor+1}")
            self.__current_floor += 1

        if direction == Direction.DOWN:
            print(f"Elevator {self.__id} is moving down to floor {self.__current_floor-1}")
            self.__current_floor -= 1



        