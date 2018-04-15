#!/usr/bin/env python

import gym
import rospy
import numpy as np
from rospy.numpy_msg import numpy_msg
from std_msgs.msg import String, UInt8
from config import GAME_CONFIG


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
            'observations_topic', String, queue_size=1)
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

    def run(self):
        self.env.render()
        observation, reward, done, info = self.env.step(self.action)

        self.cummulative_reward += reward
        self.isDone = done
        self.publish(observation, reward)

    def publish(self, observation, reward):
        # TODO: publish a matrix
        obs = [x for x in list(np.array2string(
            observation)) if x.isdigit()]
        obs = ''.join(str(e) for e in obs)
        reward = str(int(reward))
        self.pub.publish(reward[0] + obs)

    def get_cummulative_reward(self):
        return self.cummulative_reward


class Enduro(Game):

    def start(self):
        Game.start(self)
        self.prepare_environment('Enduro-v0')


class MsPacman(Game):

    def start(self):
        Game.start(self)
        self.prepare_environment('MsPacman-v0')


class CartPole(Game):

    def start(self):
        Game.start(self)
        self.prepare_environment('CartPole-v0')

games = {
    'Enduro-v0': Enduro(),
    'MsPacman-v0': MsPacman(),
    'CartPole-v0': CartPole()
}
