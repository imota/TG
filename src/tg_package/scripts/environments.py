#!/usr/bin/env python

import gym
import rospy
import numpy as np
from rospy.numpy_msg import numpy_msg
from std_msgs.msg import UInt8
from config import GAME_CONFIG
from tg_package.msg import observation_msg
from skimage import color
from PIL import Image
from skimage.transform import resize


def get_game():
    current_game = games[GAME_CONFIG['game_name']]
    current_game.start()
    return current_game


class Game(object):

    def start(self):
        self.init_ROS()
        self.action = 0
        self.cummulative_reward = 0

    def init_ROS(self):
        rospy.init_node('environment_node', anonymous=True)
        self.pub = rospy.Publisher(
            'observations_topic', observation_msg, queue_size=1)
        self.init_actuator()
        self.rate = rospy.Rate(GAME_CONFIG['game_rate'])

    def init_actuator(self):
        rospy.Subscriber('actions_topic', UInt8, self.save_action_callback)

    def prepare_environment(self, environment_name):
        self.name = environment_name
        self.env = gym.make(self.name)
        self.reset()

    def reset(self):
        observation = self.env.reset()
        self.isDone = False
        self.cummulative_reward = 0

    def save_action_callback(self, data):
        self.action = data.data
        self.game_step()

    def run(self):
        pass

    def game_step(self):
        self.env.render()
        observation, reward, done, info = self.env.step(self.action)

        self.cummulative_reward += reward
        self.isDone = done
        self.publish(observation, int(reward))

    def publish(self, observation, reward):
        message = observation_msg()
        observation = self.clean_observation(observation)

        obs = []
        for x in np.nditer(observation):
            obs.append(x)

        message.observation = obs
        message.reward = self.optimize_reward(reward)
        message.isDone = self.isDone

        self.pub.publish(message)

    def get_cummulative_reward(self):
        return self.cummulative_reward

    def optimize_reward(self, reward):
        if self.isDone:
            reward = reward - 10
        return reward  # discount for taking too long


def compact(observation, x_final, y_final, name, x_filtered, y_filtered):
    state = observation
    state = Image.fromarray(state, 'RGB')
    state.save(name + '_original.png')

    state = np.delete(state, obj=[range(x_filtered, y_filtered)], axis=0)
    state = Image.fromarray(state, 'RGB')
    state.save(name + '_filtered.png')

    state = state.convert('LA')
    state.save(name + '_grayscale.png')

    state = state.resize((x_final, y_final), Image.ANTIALIAS)
    state.save(name + '_compacted.png')

    state = np.array(state)[:, :, 0]

    img = a

    return state


class Enduro(Game):

    def start(self):
        Game.start(self)
        self.prepare_environment('Enduro-v0')
        self.observation_space = [210, 160, 3]

    def clean_observation(self, observation):
        return compact(observation, 70, 53, 'Enduro', 173, 210)


class MsPacman(Game):

    def start(self):
        Game.start(self)
        self.prepare_environment('MsPacman-v0')
        self.observation_space = [210, 160, 3]

    def clean_observation(self, observation):
        return compact(observation, 58, 53, 'Pacman', 173, 210)

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
        return compact(observation, 70, 53, 'Breakout', 0, 30)

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
        return compact(observation, 70, 53, 'Pong', 173, 210)

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
