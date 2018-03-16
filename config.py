from enum import Enum


class Games(Enum):
    ENDURO = 0
    MS_PACMAN = 1

game = Games.ENDURO

action_spaces = {
    Games.ENDURO: [0, 1, 2, 3, 4, 5, 6, 7, 8]
}

names = {
    Games.ENDURO: 'Enduro-v0'
}

GAME_CONFIG = {
    'game_rate': 10,
    'game_name': names[game],
    'action_space': action_spaces[game]
}
