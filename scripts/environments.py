#!/usr/bin/env python

import gym
import numpy as np
from config import GAME_CONFIG
from skimage import color
from PIL import Image
from skimage.transform import resize


def get_game():
    current_game = games[GAME_CONFIG['game_name']]
    current_game.start()
    return current_game

class Game(object):

    def start(self):
        self.action = 0
        self.cummulative_reward = 0

    def prepare_environment(self, environment_name):
        self.name = environment_name
        self.env = gym.make(self.name)
        self.reset()

    def play(self):
        self.reset()
        while not self.isDone:
            self.step()
        self.end()

    def reset(self):
        self.observation = self.env.reset()
        self.isDone = False
        self.cummulative_reward = 0
    
    def step(self):
        self.env.render()
        observation, reward, done, info = self.env.step(self.action)

        self.cummulative_reward += reward
        self.isDone = done

    def end(self):
        self.env.close()

    def publish(self, observation, reward):
        #message = observation_msg()
        #observation = self.clean_observation(observation)

        #obs = []
        #for x in np.nditer(observation):
        #    obs.append(x)

        #message.observation = obs
        #message.reward = self.optimize_reward(reward)
        #message.isDone = self.isDone

        #self.pub.publish(message)
        pass

    def optimize_reward(self, reward):
        #if self.isDone:
        #    reward = reward - 10 #discount for taking too long
        return reward  

    def compact(self, state, final_height, final_width):
        state = state.convert('LA')
        state = state.resize((final_height, final_width), Image.ANTIALIAS)
        state = np.array(state)[:, :, 0]

        return state

    def remove_excess(self, img, begin, end, axis):
        img = np.delete(img, obj=[range(begin, end)], axis=axis)
        img = Image.fromarray(img, 'RGB')
        return img

    def get_image(self, state):
        return Image.fromarray(state, 'RGB')


class Enduro(Game):

    def start(self):
        Game.start(self)
        self.prepare_environment('Enduro-v0')
        self.observation_space = [210, 160, 3]

    def clean_observation(self, observation):
        state = self.get_image(observation)
        state = self.remove_excess(state, 161, 210, 0)
        state = self.remove_excess(state, 0, 51, 0)
        state = self.remove_excess(state, 140, 160, 1)
        state = self.remove_excess(state, 0, 35, 1)
        return self.compact(state, 37, 35)


class MsPacman(Game):

    def start(self):
        Game.start(self)
        self.prepare_environment('MsPacman-v0')
        self.observation_space = [210, 160, 3]

    def clean_observation(self, observation):
        state = self.get_image(observation)
        state = self.remove_excess(state, 173, 210, 0)
        return self.compact(state, 58, 53)

    def optimize_reward(self, reward):
        if self.isDone:
            reward = reward - 100
        return reward - 1  # discount for taking too long


class Breakout(Game):

    def start(self):
        Game.start(self)
        self.prepare_environment('Breakout-v0')
        self.observation_space = [210, 160, 3]

    def clean_observation(self, observation):
        state = self.get_image(observation)
        state = self.remove_excess(state, 0, 30, 0)
        state = self.remove_excess(state, 155, 160, 1)
        state = self.remove_excess(state, 0, 5, 1)
        return self.compact(state, 60, 50)

    def optimize_reward(self, reward):
        if self.isDone:
            reward = reward - 100
        return reward


class Pong(Game):

    def start(self):
        Game.start(self)
        self.prepare_environment('Pong-v0')
        self.observation_space = [210, 160, 3]

    def clean_observation(self, observation):
        state = self.get_image(observation)
        state = self.remove_excess(state, 194, 210, 0)
        state = self.remove_excess(state, 0, 34, 0)
        return self.compact(state, 65, 53)

    def optimize_reward(self, reward):
        if self.isDone:
            reward = reward - 100
        return reward - 1


class Pinball(Game):

    def start(self):
        Game.start(self)
        self.prepare_environment('VideoPinball-v0')
        self.observation_space = [210, 160, 3]

    def clean_observation(self, observation):
        state = color.rgb2gray(observation)
        return state

    def optimize_reward(self, reward):
        if self.isDone:
            reward = reward - 100
        return reward


class CartPole(Game):

    def start(self):
        Game.start(self)
        self.prepare_environment('CartPole-v0')
        self.observation_space = [4]

    def clean_observation(self, observation):
        return observation

games = {
    'Enduro-v0': Enduro(),
    'MsPacman-v0': MsPacman(),
    'CartPole-v0': CartPole(),
    'Breakout-v0': Breakout(),
    'Pong-v0': Pong(),
    'VideoPinball-v0': Pinball()
}
