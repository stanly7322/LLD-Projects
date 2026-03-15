from player import Player
from board import Board
from dice import Dice


class GameLogic:
    def __init__(self, player_count, players):
        print("Welcome to Snake and Ladder Game")
        self.player_count = player_count
        self.players = players
        self.dice = Dice()
        self.board = Board()

    def add_snakes(self, start_positions, end_positions):
        for i in range(len(start_positions)):
            if start_positions[i]>end_positions[i]:
                self.board.create_snake(start_positions[i], end_positions[i])
                print("Snake " + str(i + 1) + " has been created with start position " + str(start_positions[i]) + " and end position " + str(end_positions[i]))
            else:
                print(f"start postion {start_positions[i]} and end position {end_positions[i]} are not valid")

    def add_ladders(self, start_positions, end_positions):
        for i in range(len(start_positions)):
            if end_positions[i]>start_positions[i]:
                self.board.create_ladder(start_positions[i], end_positions[i])
                print("Ladder " + str(i + 1) + " has been created with start position " + str(start_positions[i]) + " and end position " + str(end_positions[i]))
            else:
                print(f"start postion {start_positions[i]} and end position {end_positions[i]} are not valid")

    def start_game(self):
        count = 0

        while True:
            turn = count % self.player_count
            player = self.players[turn]

            player_position = player.get_position()
            print(f"Player {player.name} is at position {player_position}")

            print("It's "+ player.name + "'s turn please roll the dice")
            dice_roll = self.dice.roll()
            print("You rolled " + str(dice_roll))
            if player_position + dice_roll > self.board.size:
                new_position = player_position
            else:
                new_position = player_position + dice_roll
            final_position = self.board.check_position(new_position)
            print("Player " + str(player.name) + " is now at position " + str(final_position))

            player.set_position(final_position)

            if final_position == self.board.size:
                print("Player " + str(player.name) + " wins the game")
                break

            count+=1
            

if __name__ == "__main__":
    players_count = int(input("Enter the number of players: "))
    players = []

    for i in range(players_count):
        player_name = input("Enter the name of player " + str(i + 1) + ": ")
        player_age = int(input("Enter the age of player " + str(i + 1) + ": "))
        players.append(Player(player_name, player_age))

    game_logic = GameLogic(players_count, players)

    print("Enter the start positions of the snakes (separated by commas): ")
    start_positions = list(map(int, input().split(",")))
    print("Enter the end positions of the snakes (separated by commas): ")
    end_positions = list(map(int, input().split(",")))
    game_logic.add_snakes(start_positions, end_positions)

    print("Enter the start positions of the ladders (separated by commas): ")
    start_positions = list(map(int, input().split(",")))
    print("Enter the end positions of the ladders (separated by commas): ")
    end_positions = list(map(int, input().split(",")))
    game_logic.add_ladders(start_positions, end_positions)

    game_logic.start_game()
    
    

