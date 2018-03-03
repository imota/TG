#!/usr/bin/env python

import gym
import rospy
import numpy as np
from rospy.numpy_msg import numpy_msg
from std_msgs.msg import String
from std_msgs.msg import UInt8


class Game(object):

    def __init__(self):
        rospy.init_node('environment_node', anonymous=True)
        self.observation_pub = rospy.Publisher(
            'observations_topic', String, queue_size=1)
        rospy.Subscriber('actions_topic', UInt8, self.save_action_callback)
        self.rate = rospy.Rate(10)
        self.action = 0

    def prepare_environment(self, environment_name):
        self.name = environment_name
        self.env = gym.make(self.name)
        self.action_space = self.env.action_space
        self.isDone = False
        self.reset()

    def reset(self):
        self.observation = self.env.reset()

    def save_action_callback(self, data):
        self.action = data.data

    def run(self):
        self.env.render()
        observation, reward, done, info = self.env.step(self.action)

        self.observation = observation
        self.isDone = done
        self.publish_observation()

    def publish_observation(self):
        self.observation_pub.publish(np.array2string(self.observation))


class Enduro(Game):

    def __init__(self):
        Game.__init__(self)
        self.prepare_environment('Enduro-v0')


class MsPacman(Game):

    def __init__(self):
        super(Game, self).__init__()
        self.prepare_environment('MsPacman-v0')


class CartPole(Game):

    def __init__(self):
        super(Game, self).__init__()
        self.prepare_environment('CartPole-v0')
