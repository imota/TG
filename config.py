from enum import Enum


class Games(Enum):
    ENDURO = 0
    MS_PACMAN = 1

game = Games.ENDURO

action_spaces = {
    Games.ENDURO: 8
}

names = action_spaces = {
    Games.ENDURO: 'Enduro-v0'
}

GAME_CONFIG = {
    'game_rate': 10,
    'game_name': names[game],
    'action_space': action_spaces[game]
}
