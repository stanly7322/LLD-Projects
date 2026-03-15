class Board:
    def __init__(self):
        self.size = 9
        self.blocks = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def print_board(self):
        for i in range(3):
            print(" | ".join(str(x) if x != 0 else " " for x in self.blocks[i]))
            if i < 2:
                print("--+---+--")

    def mark_block(self, position, id):
        if position > 9 or position < 1:
            print("postition Invalid")
            return position
        
        x, y = self.__get_coordinates(position)
        
        if self.blocks[x][y] == 0:
            self.blocks[x][y] = id
            return position
        
        print("Positon already Marked")
        return position
    
    def check_vacant(self):
        for i in self.blocks:
            for j in i:
                if j != 0:
                    return True
            
        return False
    
    def check_win(self, position, id):
        x, y = self.__get_coordinates(position)

        # Check row
        if all(self.blocks[x][col] == id for col in range(3)):
            return True

        # Check column
        if all(self.blocks[row][y] == id for row in range(3)):
            return True

        # Check main diagonal
        if x == y:
            if all(self.blocks[i][i] == id for i in range(3)):
                return True

        # Check anti-diagonal
        if x + y == 2:
            if all(self.blocks[i][2 - i] == id for i in range(3)):
                return True

        return False


    def __get_coordinates(self, position):
        # x -> row, y -> col
        position = position - 1
        x = position // 3
        y = position % 3
        return x, y
            
        


