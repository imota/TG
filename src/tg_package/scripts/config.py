from enum import Enum


class Games(Enum):
    ENDURO = 0
    MS_PACMAN = 1
    CART_POLE = 2
    BREAKOUT = 3

game = Games.BREAKOUT

state_sizes = {
    Games.ENDURO: 33600,
    Games.MS_PACMAN: 33600,
    Games.CART_POLE: 4,
    Games.BREAKOUT: 33600
}

action_spaces = {
    Games.ENDURO: [0, 1, 2, 3, 4, 5, 6, 7, 8],
    Games.MS_PACMAN: [0, 1, 2, 3, 4, 5, 6, 7, 8],
    Games.CART_POLE: [0, 1],
    Games.BREAKOUT: [0, 1, 2, 3]
}

names = {
    Games.ENDURO: 'Enduro-v0',
    Games.MS_PACMAN: 'MsPacman-v0',
    Games.CART_POLE: 'CartPole-v0',
    Games.BREAKOUT: 'Breakout-v0'
}

GAME_CONFIG = {
    'game_rate': 33,
    'game_name': names[game],
    'action_space': action_spaces[game],
    'state_size': state_sizes[game]
}
