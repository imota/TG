#!/usr/bin/env python

import rospy
import random
import numpy as np
from std_msgs.msg import String, UInt8
from config import GAME_CONFIG

from sklearn.neural_network import MLPRegressor


class Policy(object):

    def __init__(self, action_space):
        self.action_space = action_space
        self.gamma = 0.618
        self.cummulative_reward = 0
        self.random_factor = 0.9

        self.clf = MLPRegressor(solver='lbfgs', alpha=1e-5,
                                hidden_layer_sizes=(5, 2), random_state=1)
        x_train = np.array([0 for i in range(180)])
        y_train = np.array([random.randrange(0, 10)
                            for i in range(len(self.action_space))])
        self.clf.fit(x_train.reshape(1, -1), y_train.reshape(1, -1))

    def get_random_action(self, probability):
        if self.random_factor > 0.1:
            self.random_factor = self.random_factor - 0.00001
            print self.random_factor
        return random.random() < probability

    def get_action(self, state):
        if state != None:
            if not self.get_random_action(self.random_factor):
                state = [int(x) for x in [state[i] for i in range(180)]]
                state = np.array(state)
                action = np.argmax(self.clf.predict(state.reshape(1, -1)))
                return action
            print 'random'
        return random.choice(self.action_space)

    def train_neural_network(self, state, action, reward):
        if state != None:
            state = [float(x) for x in [state[i] for i in range(180)]]
            state = np.array(state)
            reward_before_training = self.clf.predict(state.reshape(1, -1))

            reward_after_feedback = reward_before_training
            reward_after_feedback[0][action] = reward + \
                self.gamma * reward_before_training[0][action]
            self.clf.fit(state.reshape(1, -1),
                         reward_after_feedback.reshape(1, -1))


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
        reward = int(observation.data[0]) * 10

        self.pi.train_neural_network(
            self.current_state, self.prev_action, reward)

        self.cummulative_reward += reward
        self.current_state = observation.data
        self.prev_action = action

        self.action_pub.publish(action)

if __name__ == '__main__':
    agent = Agent()
