from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)

def read_lines(filename):
    try: 
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        return lines
    except FileNotFoundError:
        print("{} does not exist!".format(filename))
        exit()

def parse(lines):
    stripped_ls = []
    i = 0
    while i < len(lines):
        # removes \n all throughout list of strings
        stripped_ls.append((lines[i]).strip())
        i += 1 

    start = "X"
    end = "Y"
    air = " "
    wall = "*"
    fire = "F"
    water = "W"

    final_ls = []
    i = 0
    start_count = 0
    end_count = 0
    # create array length of 9 for no.1-9 teleport pads
    # increment respective index if it exists, eg. no.1 teleport pad --> index 0
    teleport_count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    while i < len(stripped_ls):
        j = 0
        ls = []
        while j < len(stripped_ls[i]):
            if stripped_ls[i][j] == start:
                ls.append(Start())
                start_count += 1
            elif stripped_ls[i][j] == end:
                ls.append(End())
                end_count += 1
            elif stripped_ls[i][j] == air:
                ls.append(Air())
            elif stripped_ls[i][j] == wall:
                ls.append(Wall())
            elif stripped_ls[i][j] == fire:
                ls.append(Fire())
            elif stripped_ls[i][j] == water:
                ls.append(Water())
            elif stripped_ls[i][j] in "123456789":
                ls.append(Teleport(stripped_ls[i][j]))
                # eg. num is 3 = 3 - 1 = increment at index 2
                teleport_index = int(stripped_ls[i][j]) - 1
                teleport_count[teleport_index] += 1
            else:
                raise ValueError("Bad letter in configuration file: {}.".format(stripped_ls[i][j]))
            j += 1
        final_ls.append(ls)
        i += 1

    if start_count != 1:
        raise ValueError("Expected 1 starting position, got {}.".format(start_count))
    if end_count != 1:
        raise ValueError("Expected 1 ending position, got {}.".format(end_count))

    i = 0
    while i < len(teleport_count):
        # teleport_count[i] not in [0, 2]
        # if value at specific index is not 0 or 2 --> raise ValueError
        if teleport_count[i] != 0 and teleport_count[i] != 2:
            raise ValueError("Teleport pad {} does not have an exclusively matching pad.".format(i + 1))
        i += 1

    return final_ls

# finds the start coordinates for player's intial position
def get_start_coordinates(lines):
    start = "X"
    i = 0
    start_row = 0
    start_col = 0
    while i < len(lines):
        j = 0
        while j < len(lines[i]):
            if lines[i][j] == start:
                start_row += i
                start_col += j
            j += 1
        i += 1
    
    return start_row, start_col
