from player import Player
from board import Board


class GameLogic:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]

    def start_game(self):
        count = 0

        while True:

            turn = count%2
            player = self.players[turn]

            print(f"Player {player.name} it is your turn")
            position = int(input("Enter position blw 1 to 9: "))

            final_position = self.board.mark_block(position, player.id)
            print(f"Player {player.name} marked {final_position}")

            self.board.print_board()

            if self.board.check_win(position, player.id):
                print(f"Hurray Player {player.name} wins")
                break
            
            if not self.board.check_vacant():
                print("The game is a draw")
                break
            
            count += 1

if __name__ == "__main__":
    print("Welcome to Tic Tac Toe Game")

    player_name_1 = input("Enter the name of player 1 : ")
    player_age_1 = int(input("Enter the age of player 1 : "))

    player_1 = Player(player_name_1, player_age_1, 1)

    player_name_2 = input("Enter the name of player 2 : ")
    player_age_2 = int(input("Enter the age of player 2 : "))

    player_2 = Player(player_name_2, player_age_2, 2)

    game_logic = GameLogic(player_1, player_2)

    game_logic.start_game()
