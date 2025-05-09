from player import Player

def grid_to_string(grid, player):
    final_string = ""
    i = 0
    while i < len(grid):
        j = 0
        string = ""
        while j < len(grid[i]):
            if i == player.row and j == player.col:
                string += player.display
            else:
                string += grid[i][j].display
            j += 1
        final_string += string + "\n"
        i += 1
    
    if player.num_water_buckets == 1:
        final_string = ("{}\nYou have {} water bucket.".format(final_string, player.num_water_buckets))
    if player.num_water_buckets == 0 or player.num_water_buckets > 1:
        final_string = ("{}\nYou have {} water buckets.".format(final_string, player.num_water_buckets))

    return final_string