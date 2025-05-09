from game import Game
import os
import sys

filename = sys.argv[1]
game = Game(filename)

# function prints what moves were made and number of moves made
def print_moves():
    if len(game.ls_of_moves_made) == 1:
        print("\nYou made 1 move.")
        print("Your move: ", end="")
    else:
        print("\nYou made {} moves.".format(game.num_of_moves_made))
        print("Your moves: ", end="")
    i = 0
    while i < len(game.ls_of_moves_made):
        if i == len(game.ls_of_moves_made) - 1:
            print(game.ls_of_moves_made[i].lower())
        else:
            print(game.ls_of_moves_made[i].lower(), end=", ")
        i += 1

good_input = ["w", "a", "s", "d", "e", "W", "A", "S", "D", "E"]

print(game.get_grid())
move = input("\nInput a move: ")

taking_input = True
while taking_input:
    # quits the game
    if move == "q":
        print("\nBye!")
        sys.exit()
    # bad input
    elif move not in good_input:
        print(game.get_grid())
        print("\nPlease enter a valid move (w, a, s, d, e, q).")
        move = input("\nInput a move: ")
    # good input
    else:
        message = game.game_move(move)
        print(game.get_grid())
        if message:
            print("\n" + message)

        # check if game has ended
        if game.successful_game_end:
            print_moves() 
            print("\n=====================")
            print("====== YOU WIN! =====")
            print("=====================")
            break
        elif game.unsuccessful_game_end:
            print_moves() 
            print("\n=====================")
            print("===== GAME OVER =====")
            print("=====================")
            break
            
        # if game hasn't end, keeping going
        move = input("\nInput a move: ")
