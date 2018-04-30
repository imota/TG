from enum import Enum


class Games(Enum):
    ENDURO = 0
    MS_PACMAN = 1
    CART_POLE = 2

game = Games.MS_PACMAN

action_spaces = {
    Games.ENDURO: [0, 1, 2, 3, 4, 5, 6, 7, 8],
    Games.MS_PACMAN: [0, 1, 2, 3, 4, 5, 6, 7, 8],
    Games.CART_POLE: [0, 1]
}

names = {
    Games.ENDURO: 'Enduro-v0',
    Games.MS_PACMAN: 'MsPacman-v0',
    Games.CART_POLE: 'CartPole-v0'
}

GAME_CONFIG = {
    'game_rate': 10,
    'game_name': names[game],
    'action_space': action_spaces[game]
}

observation_size = {
    Games.ENDURO: 162,
    Games.MS_PACMAN: 180,
    Games.CART_POLE: 100800
}