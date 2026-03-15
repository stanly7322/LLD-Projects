from snake import Snake
from ladder import Ladder

class Board:
    def __init__(self):
        self.size = 100
        self.snakes = {}
        self.ladders = {}

    def create_snake(self, start_position, end_position):
        snake = Snake(start_position, end_position)
        self.snakes[snake.get_start_position()] = snake.get_end_position()
        return snake
    
    def create_ladder(self, start_position, end_position):
        ladder = Ladder(start_position, end_position)
        self.ladders[ladder.get_start_position()] = ladder.get_end_position()
        return ladder
    
    def check_position(self, position):
        if position in self.snakes:
            print("snakes swallowed you are moving down to " + str(self.snakes[position]))
            return self.snakes[position]
        
        if position in self.ladders:
            print("Hurray found Ladder moving up to " + str(self.ladders[position]))
            return self.ladders[position]
        
        return position