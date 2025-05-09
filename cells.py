class Start:
    def __init__(self):
        self.display = "X"

    def step(self, game, row, col):
        game.player.move(row, col)
        return None

class End:
    def __init__(self):
        self.display = "Y"

    def step(self, game, row, col):
        game.player.move(row, col)
        # end game
        return game.successful_game("\nYou conquer the treacherous maze set up by " \
                                    "the Fire Nation and reclaim the Honourable " \
                                    "Furious Forest Throne, restoring your hometown " \
                                    "back to its former glory of rainbow and " \
                                    "sunshine! Peace reigns over the lands.")

class Air:
    def __init__(self):
        self.display = " "

    def step(self, game, row, col):
        game.player.move(row, col)
        return None

class Wall:
    def __init__(self):
        self.display = "*"

    def step(self, game, row, col):
        return "You walked into a wall. Oof!"

class Fire:
    def __init__(self):
        self.display = "F"

    def step(self, game, row, col):
        game.player.move(row, col)
        if game.player.num_water_buckets == 0:
            # end game
            return game.unsuccessful_game("\nYou step into the fires and watch your " \
                                          "dreams disappear :(.\n" \
                                          "\nThe Fire Nation triumphs! The Honourable " \
                                          "Furious Forest is reduced to a pile of ash " \
                                          "and is scattered to the winds by the next " \
                                          "storm... You have been roasted.")
        else:
            # fire block should behave like an air block
            game.replace_with_cell(row, col, Air())
            game.player.num_water_buckets -= 1
            return ("With your strong acorn arms, you throw a water bucket at the " \
                    "fire. You acorn roll your way through the extinguished flames!")

class Water:
    def __init__(self):
        self.display = "W"

    def step(self, game, row, col):
        game.player.move(row, col)
        # water block should behave like an air block
        game.replace_with_cell(row, col, Air())
        game.player.num_water_buckets += 1
        return "Thank the Honourable Furious Forest, you've found a bucket of water!"

class Teleport:
    def __init__(self, num):
        self.display = num

    def step(self, game, row, col):
        # find out where the player should teleport to
        object_at_pos = game.object_ls[row][col]
        
        new_row = 0
        new_col = 0
        if object_at_pos.display in "123456789":
            i = 0
            while i < len(game.object_ls):
                j = 0
                while j < len(game.object_ls[i]):
                    if object_at_pos.display == game.object_ls[i][j].display:
                        if row != i or col != j:
                            new_row = i
                            new_col = j
                    j += 1
                i += 1
        
        game.player.move(new_row, new_col)
        return ("Whoosh! The magical gates break Physics as we know it "
                "and opens a wormhole through space and time.")
