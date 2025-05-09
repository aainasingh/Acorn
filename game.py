from game_parser import read_lines, parse, get_start_coordinates
from grid import grid_to_string
from player import Player

class Game:
    def __init__(self, filename):
        lines = read_lines(filename)
        row, col = get_start_coordinates(lines)

        self.object_ls = parse(lines)
        self.player = Player(row, col)
        self.successful_game_end = False
        self.unsuccessful_game_end = False
        self.ls_of_moves_made = []
        self.num_of_moves_made = 0

    def game_move(self, move):
        row, col = self.get_next_pos_for_move(move)

        object_at_pos = self.object_ls[row][col]
        
        # if next cell is a wall, don't append the move
        if object_at_pos.display != "*" and row >= 0 and col >= 0:
            self.ls_of_moves_made.append(move)
            self.num_of_moves_made += 1
        
        # check if row and col are negative
        if row < 0 or col < 0:
            return "You walked into a wall. Oof!"
        
        message = object_at_pos.step(self, row, col)

        return message

    def get_grid(self):
        return grid_to_string(self.object_ls, self.player)

    # finds next the cell's row and col depending on the move
    def get_next_pos_for_move(self, move):
        row = self.player.row
        col = self.player.col

        if move == "w" or move == "W":
            row -= 1
        elif move == "a" or move == "A":
            col -= 1
        elif move == "s" or move == "S":
            row += 1
        elif move == "d" or move == "D":
            col += 1
        elif move == "e" or move == "E":
            pass

        return row, col

    def replace_with_cell(self, row, col, cell):
        self.object_ls[row][col] = cell

    def successful_game(self, message):
        self.successful_game_end = True
        return message

    def unsuccessful_game(self, message):
        self.unsuccessful_game_end = True
        return message
