#!/usr/bin/env python

import gym
import rospy
import numpy as np
from rospy.numpy_msg import numpy_msg
from std_msgs.msg import String

class Game(object):
    def __init__(self):
        rospy.init_node('environment_node', anonymous=True)
        self.observation_pub = rospy.Publisher('observations_topic', String, queue_size=1)
        self.rate = rospy.Rate(10)
        pass

    def prepare_environment(self, environment_name):
        self.name = environment_name
        self.env = gym.make(self.name)
        self.action_space = self.env.action_space
        self.isDone = False
        self.reset()   

    def reset(self):
        self.observation = self.env.reset()

    def select_action(self):
        return self.action_space.sample()

    def run(self):
        self.env.render()
        action = self.select_action()
        observation, reward, done, info = self.env.step(action)

        self.observation = observation
        self.isDone = done
        self.publish_observation()
        
        self.rate.sleep()

    def publish_observation(self):
        self.observation_pub.publish(np.array2string(self.observation))

    def publish_reward(self):
        pass

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