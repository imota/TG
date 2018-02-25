#!/usr/bin/env python

import game

class Policy(object):
    def __init__(self, action_space):
        self.action_space = action_space

class Agent(object):
    def __init__(self, game):
        self.game = game

if __name__ == '__main__':
    game = game.Enduro()
    for i_episode in range(20):
        game.reset()
        for t in range(1000):
            game.run()
            if game.isDone:
                break