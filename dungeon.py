"""
Group Members: lauren in progress
"""

# DO NOT CHANGE OR REMOVE THE FOLLOWING LINES
import random
import utilities
# DO NOT CHANGE OR REMOVE THE PRECEDING LINES

MAP_SQUARE_CHASM = 'O'
MAP_SQUARE_EMPTY = ' '
MAP_SQUARE_HEALTH = '+'
MAP_SQUARE_KEY = 'k'
MAP_SQUARE_LOCK = '@'
MAP_SQUARE_PEBBLE = '.'
MAP_SQUARE_PEBBLES = ':'
MAP_SQUARE_PLANK = '='
MAP_SQUARE_PLANK_SET = 'I'
MAP_SQUARE_ROCK = '#'
MAP_SQUARE_ROPE = '&'
MAP_SQUARE_ROPE_TIED = '~'
MAP_SQUARE_SLINGSHOT = 'Y'


width = -1
height = -1
dungeon_map = []  # NOTE: Each square in the map is a one-character string. Each row is a list of squares. The map is a list of rows.


def get_map_square(x, y):
    """
    Returns the map square at the location (x, y).
    The value returned for invalid coordinates is a rock.
    :param x: int, horizontal index in the map
    :param y: int, vertical index in the map
    :return: str, single character
    """
    result = MAP_SQUARE_ROCK
    if ((x >=0 and x< width) and (y>= 0 and y< height)):  # LT i think done TODO: Replace False with a condition that checks if the values x and y are valid. Valid index values start at 0. x must be less than width and y must be less than height. Negative numbers are not valid.
        row= dungeon_map[y]
        result= row[x]  # LT... done? see bitmap hw in comments below TODO: Replace None with an expression that uses x and y to get the right value from dungeon_map. 
    return result

# from our bitmap homework:
# What if we want to know what the pixel is at a given (x, y) location?
# def get_pixel(bitmap, x, y):
    #row = bitmap[y] # pick the row from the bitmap
    #return row[x]   # get the character in the row

#print('What\'s the pixel at (3, 5)?')
# get_pixel(SAMPLE_BITMAP, 3, 5)

def set_map_square(x, y, current_value, new_value):
    """
    Updates the square at location (x, y) with a new value.
    Validates that the caller has first checked the current value
    by comparing the parameter current_value the actual current value.
    Only if the values of x, y, and current_value are valid does the udpate happen.
    :param x: int, horizontal index in the map
    :param y: int, vertical index in the map
    :param current_value: str, single character
    :param new_value: str, single character
    :return: True if update happened, False if update did not happen
    """
    result = False
    if False:  # TODO: Replace False with a condition that checks if x and y are valid map index values and also checks that current_value matches the square in the map at location (x, y).
        # TODO: Update the correct (x, y) location in dungeon_map with new_value.
        result = True
    return result

# from bitmap homework again:
#def set_pixel(bitmap, x, y, character):
    #row = bitmap[y]    # pick a row from the bitmap
    #row[x] = character # set character in the row


def clear_map_square(x, y, current_value):
    """
    Uses the set_map_square() function to set the square to empty.
    :param x: int, horizontal index in the map
    :param y: int, vertical index in the map
    :param current_value: str, single character
    :return: True if update happened, False if update did not happen
    """
    return set_map_square(x, y, current_value, MAP_SQUARE_EMPTY)


def draw_map_row(center_x, center_y, row_offset, screen_radius, player_symbol, werewolf):
    """
    Returns a string to display for what the map should look like on this row of the screen.
    :param center_x: int, horizontal index in the map that should be at the center of the screen
    :param center_y: int, vertical index in the map that should be at the center of the screen
    :param row_offset: int, which row of the screen is being displayed (top row is 0)
    :param screen_radius: int, how many characters to show between the center of the map and the edge of the map
    :param player_symbol: str, one character representing the player
    :param werewolf: werewolf module
    :return: str, a portion of the map to display
    """
    result = ""  # The result is a string that we are building one character at a time, going from left to right across the screen in a single row.
    row = center_y - screen_radius + row_offset
    for column in range(center_x - screen_radius, center_x + screen_radius + 1):
        # TODO: If the current column and row values match (center_x, center_y) then the player's symbol is the next character in the result, else...
        # TODO: If the current column and row values match the werewolf's location then the werewolf's symbol is the next character in the result, else...
        # TODO: Otherwise, the next character in the result is the map square at the location matching the row and column.
        pass
    return result


def load_game(filename):
    """
    Loads a file with the given filename.
    :param filename: str, name of file to load
    :return: tuple of player and werewolf data if file is valid, or False if file is invalid
    """
    global width, height, dungeon_map  # DO NOT REMOVE

    try:
        with open(filename, 'r') as file_handler:
            file_text = None  # TODO: Replace None so that file_text contains all the text in the file.
    except FileNotFoundError as error:
        return False

    lines = file_text.split('\n')
    line = None  # TODO: Replace None so that your code removes the first string in the list lines and stores it in the variable line.
    temp_width, temp_height, player_x, player_y, player_symbol, werewolf_x, werewolf_y, werewolf_health, werewolf_stun_count = None
    # TODO: Replace None on the preceding line of code. Extract values for all of these variables from the variable line.
    # TODO: All of the variables on the line above EXCEPT player_symbol need to be integers, not strings.

    temp_dungeon_map = []  # Store the dungeon map from the file in a temporary variable before we decide to throw out our old map.
    while len(temp_dungeon_map) < temp_height and len(lines) > 0:
        row = None  # TODO: Replace None so that your code removes the first string in the list lines and stores it in the variable row.
        if row != '':
            temp_dungeon_map.append(list(row))  # What does list do here?
    squares = 0
    for row in temp_dungeon_map:  # Count up the number of squares in the file's map.
        squares += len(row)
    if squares != temp_width * temp_height:
        # Validation: If the number of squares in the dungeon map does not match the width and height values in the file, that is a problem.
        return False

    # The data from the file is valid so now we can update the real width, height, and dungeon_map variables.
    width = temp_width
    height = temp_height
    dungeon_map = temp_dungeon_map

    player_inventory = {}
    for line in lines:
        # TODO: Extract from the remaining lines of text in the file data for the player's inventory.
        #       Each line of the inventory data has a single character for the item, followed by a space, followed by the count for that item.
        #       Store the data in the player_inventory dictionary; each key in the dictionary is an item, and its matching value is the numeric count.
        pass

    # TODO: Return a tuple of values (that you got in his function) so that the order of the values matches the order in the tuple returned by load_default_game().


def load_default_game():
    """
    Loads the default game.
    :return: tuple of player and werewolf data
    """
    global width, height, dungeon_map  # DO NOT REMOVE
    width = 5
    height = 3
    dungeon_map = [list("&.@:="), list("     "), list("OYO k")]
    return (
        2,    # player x
        1,    # player y
        '>',  # player symbol
        {'+': 1}, # inventory
        0,    # werewolf x
        1,    # werewolf y
        1,    # werewolf health
        0,    # werewolf stun count
    )


def save_game(filename, player_x, player_y, player_symbol, inventory, werewolf):
    """
    Saves game data to a file with the given filename.
    :param filename: str, name of file to save
    :param player_x: int, player's x coordinate (horizontal index in the map)
    :param player_y: int, player's y coordinate (vertical index in the map)
    :param player_symbol: str, one character representing the direction the player is looking
    :param inventory: dict, player's inventory
    :param werewolf: werewolf module
    :return: True if game was saved successfully, False if game was not saved successfully
    """
    global width, height, dungeon_map  # DO NOT REMOVE
    try:
        with open(filename, 'w') as file_handler:
            # TODO: Write the game data to the file with the given filename.
            #  - the first row contain's the dungeon width and height, followed by player data, followed by werewolf data
            #  - then write the dungeon map to the file
            #  - then write the player's inventory to the map
            pass
    except:
        return False
    return True


def get_random_empty_location(player_x, player_y, min_distance_from_player):
    """
    Returns a random empty location in the dungeon that is at least min_distance_from_player from the location (player_x, player_y).
    :param player_x: int, player's x coordinate (horizontal index in the map)
    :param player_y: int, player's y coordinate (vertical index in the map)
    :param min_distance_from_player: int, minimum distance from player that makes an empty square eligible to be chosen
    :return: tuple of (x, y) if a valid empty location is found, or None if no valid locations can be found
    """
    empty_locations = []
    for row in range(height):
        for column in range(width):
            if False:  # TODO: Replace False with condition that checks that location (column, row) is empty and at least min_distance_from_player squares from the player.
                # TODO: Add the empty location tuple to the list of empty locations.
                pass
    # TODO: If the list of empty locations is empty, return None.
    # TODO: Otherwise, return one of the location tuples from the list.


def are_these_two_locations_visible_to_each_other(first_x, first_y, second_x, second_y, can_see_past_function):
    """
    Answers the question of whether someone at location (first_x, first_y) could see someone or something at location (second_x, second_y).
    There are different rules for who can see past what, so the caller provides a can_see_past_function to help us decide.
    :param first_x: int, horizontal index in the map
    :param first_y: int, vertical index in the map
    :param second_x: int, horizontal index in the map
    :param second_y: int, vertical index in the map
    :param can_see_past_function: function, returns True/False for whether the viewer can see past the square at location (x, y)
    :return: True if can see from (first_x, first_y) to (second_x, second_y), or False if cannot
    """
    are_visible = True
    if first_x == second_x:
        direction = utilities.sign(second_y - first_y)
        for i in range(first_y + direction, second_y, direction):
            if not can_see_past_function(first_x, i):
                are_visible = False
                break
    elif first_y == second_y:
        direction = utilities.sign(second_x - first_x)
        for i in range(first_x + direction, second_x, direction):
            if not can_see_past_function(i, first_y):
                are_visible = False
                break
    else:
        are_visible = False
    return are_visible
