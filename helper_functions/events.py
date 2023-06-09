"""
Adam Goldsmith
A01185566
"""
import random
from helper_functions.chest import chest
from helper_functions.shop import shop
from helper_functions.battle import battle
from helper_functions.boss import boss_battle
from helper_functions.nymph import nymph


def all_events(board: dict, character: dict, region: list) -> None:
    """
    Create event dictionary

    :param board: A dictionary
    :param character: A dictionary
    :param region: A list
    :precondition: Board must be a dictionary created by the create_board() function
    :preconditon: Character must be a dictionary created by the create_character() function
    :precondition: Region must be a list created by the get_region() function
    :postcondition: start an event of a certain event type
    """
    if type(board) is not dict or type(character) is not dict or type(region) is not list:
        raise TypeError("Arguments must be correct data types")
    events = {
        'chest': chest,
        'nymph': nymph,
        'enemy': battle,
        'shop': shop,
        'boss': boss_battle,
    }
    character_location = (character['X-coordinate'], character['Y-coordinate'])
    if board[character_location] == 'chest' or board[character_location] == 'nymph':
        events[board[character_location]](character)
        board[character_location] = 'empty'
    elif board[character_location] == 'shop':
        events['shop'](character)
    elif board[character_location] == 'boss':
        events['boss'](character, region)
    elif board[character_location] == 'empty' or board[character_location] == 'start':
        if random.randint(1, 4) == 1:
            events['enemy'](character)
    else:
        raise KeyError("Board tile does not exist.")
    