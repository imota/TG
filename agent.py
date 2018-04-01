#!/usr/bin/env python

import rospy
import random
import numpy as np
from std_msgs.msg import String, UInt8
from config import GAME_CONFIG

from sklearn.neural_network import MLPClassifier


class Policy(object):

    def __init__(self, action_space):
        self.action_space = action_space
        self.gamma = 0.618
        self.cummulative_reward = 0
        # TODO: iniciar a rede neural
        #   np.zeros([env.observation_space.n, env.action_space.n])
        self.clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                                 hidden_layer_sizes=(5, 2), random_state=1)
        # TODO: iniciar o estado inicial self.current_state = 0

    def get_action(self, state):
        return random.choice(self.action_space)
        # TODO: return np.argmax(Q[state])

    def train_neural_network(self, state, action, reward):
        # Q[state, action] = (reward + gamma * np.max(Q[state2]))
        pass


class Agent(object):

    def __init__(self):
        self.pi = Policy(GAME_CONFIG['action_space'])
        self.prev_action = 0
        self.cummulative_reward = 0
        self.current_state = None
        self.init_ROS()

    def init_ROS(self):
        rospy.init_node('agent_node', anonymous=True)
        self.action_pub = rospy.Publisher('actions_topic', UInt8, queue_size=1)
        rospy.Subscriber('observations_topic', String, self.select_action)
        self.rate = rospy.Rate(GAME_CONFIG['game_rate'])
        rospy.spin()

    def select_action(self, observation):
        action = self.pi.get_action(observation.data[1:])
        reward = int(observation.data[0])

        self.pi.train_neural_network(
            self.current_state, self.prev_action, reward)

        self.cummulative_reward += reward
        self.current_state = observation
        self.prev_action = action

        self.action_pub.publish(action)

if __name__ == '__main__':
    agent = Agent()
