"""
Group Members:
"""

# DO NOT CHANGE OR REMOVE THE FOLLOWING LINE
import random
import dungeon
import utilities
# DO NOT CHANGE OR REMOVE THE PRECEDING LINE

WEREWOLF_SYMBOL_NORMAL = 'W'
WEREWOLF_SYMBOL_STUNNED = 'w'
WEREWOLF_SYMBOL_DEAD = 'm'
WEREWOLF_MAX_DAMAGE = 5
WEREWOLF_POST_ATTACK_MIN_TELEPORT_DISTANCE = 6
WEREWOLF_PICTURE_WIDTH = 36
WEREWOLF_PICTURE_HEIGHT = 12

x = -1
y = -1
health = 0
stunned_count = 0
skip_turn = False


def is_alive():
    """
    Tells whether the werewolf is alive.
    :return: bool, True if health is greater than zero, or False if not
    """
    return False  # TODO: Replace False with the necessary condition. See description.


def is_stunned():
    """
    Tells whether werewolf is stunned.
    :return: bool, True if stunned_count is greater than zero, or False if not
    """
    return False  # TODO: Replace False with the necessary condition. See description.


def get_symbol():
    """
    Returns the symbol that should be used to represent the werewolf's physical state.
    If the werewolf is dead, returns WEREWOLF_SYMBOL_DEAD.
    If the werewolf is alive and stunned, returns WEREWOLF_SYMBOL_STUNNED.
    If the werewolf is alive and not stunned, returns WEREWOLF_SYMBOL_NORMAL.
    :return: str, single character representing werewolf's physical state
    """
    # TODO: Return the correct value. See description.
    pass


def do_hit(points_of_damage):
    """
    Applies damage to werewolf's health, increases stun count, and returns the health value.
    :param points_of_damage: int, points of damage to remove from health
    :return: int, health after damage is applied
    """
    # TODO: Decrease the werewolf's health by points_of_damage.
    # TODO: Make sure the werewolf's health is not below 0. Negative health is a silly idea.
    # TODO: Increase the stun count by 2.
    # TODO: Return the value of the werewolf's health.
    pass


def do_next_move(player_x, player_y):
    """
    Perform the werewolf's next move.
    :param player_x: int, x coordinate of where the werewolf thinks the player is
    :param player_y: int, y coordinate of where the werewolf thinks the player is
    """
    global x, y, stunned_count, skip_turn
    # TODO: If the werewolf is dead, exit this function.
    # TODO: If we should skip the werewolf's turn, set skip to False and exit this function.
    # TODO: If werewolf is stunned, decrease the stun count by 1 and exit this function.

    delta_x = player_x - x  # distance from werewolf to player in X direction
    delta_y = player_y - y  # distance from werewolf to player in Y direction

    possible_next_x = x + utilities.sign(delta_x)  # one square closer to player in X direction
    possible_next_y = y + utilities.sign(delta_y)  # one square closer to player in Y direction

    is_x_direction_move_possible = delta_x != 0 and is_open_space(possible_next_x, y)
    is_y_direction_move_possible = delta_y != 0 and is_open_space(x, possible_next_y)

    if is_x_direction_move_possible and not is_y_direction_move_possible:
        x = possible_next_x  # If werewolf can only move horizontally, then do so.
    elif not is_x_direction_move_possible and is_y_direction_move_possible:
        y = possible_next_y  # If werewolf can only move vertically, then do so.
    elif is_x_direction_move_possible and is_y_direction_move_possible:
        if abs(delta_x) > abs(delta_y):
            x = possible_next_x  # If werewolf can move in both directions but is closer horizontally, move horizontally.
        elif abs(delta_x) < abs(delta_y):
            y = possible_next_y  # If werewolf can move in both directions but is closer vertically, move vertically.
        else:
            # If werewolf can move in both directions and is equally close to the player horizontally and vertically, randomly pick whether to move horizontally or vertically.
            randomly_pick_x = random.choice([True, False])
            if randomly_pick_x:
                x = possible_next_x
            else:
                y = possible_next_y


def is_open_space(possible_x, possible_y):
    """
    Tells whether the map square at location (possible_x, possible_y) is an open space for the werewolf.
    An open space is a type of square that the werewolf can walk over or through.
    The werewolf can walk through empty squares, step on a key, step on a pebble, step on multiple pebbles,
    walk on a free plank, walk across set planks, and step on free rope.
    :param possible_x: int, horizontal index in map
    :param possible_y: int, vertical index in map
    :return: bool, True if werewolf can walk over or through this location, or False otherwise
    """
    # TODO: Return the correct value based on the description.
    pass
