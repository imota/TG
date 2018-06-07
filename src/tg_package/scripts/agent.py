#!/usr/bin/env python

import rospy
import random
import numpy as np
from std_msgs.msg import UInt8
from config import GAME_CONFIG
from tg_package.msg import observation_msg

from sklearn.neural_network import MLPRegressor
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras import optimizers


class PolicyOfSingleOutput(object):

    def __init__(self, action_space):
        self.action_space = action_space
        self.gamma = 0.618
        self.alpha = 0.9
        self.state_size = GAME_CONFIG['state_size']

        self.initiate_Qfunction()

    def initiate_Qfunction(self):

        observation_train = np.array([0 for i in range(self.state_size)])
        action_train = np.array([0 for i in range(len(self.action_space))])
        x_train = np.concatenate((observation_train, action_train), axis=0)
        y_train = np.array([0.0])

        self.model = Sequential()
        self.model.add(Dense(24, input_dim=self.state_size +
                             len(self.action_space), activation='relu'))
        self.model.add(Dense(24, activation='relu'))
        self.model.add(Dense(1, activation='linear'))
        self.model.compile(loss='mse',
                           optimizer=optimizers.Adam(lr=self.alpha))

        self.model.fit(x_train.reshape(1, -1), y_train, epochs=1, verbose=0)

    def get_action(self, state):
        if state != None:
            state = np.array(state)
            return self.maxQ_action(state)
        return 0

    def _maxQ(self, state):
        max_action, max_reward = 0, 0
        for action in self.action_space:
            actions_array = np.array(
                [0 for i in range(len(self.action_space))])
            actions_array[action] = 1

            input = np.concatenate((state, actions_array), axis=0)
            reward = self.model.predict(input.reshape(1, -1))
            print action, reward
            if reward >= max_reward:
                max_action = action
                max_reward = reward
        return action, reward

    def maxQ_reward(self, state):
        return self._maxQ(state)[1]

    def maxQ_action(self, state):
        return self._maxQ(state)[0]

    def train(self, state, action, reward, next_state):
        if state != None:
            state = np.array(state)
            actions_array = np.array(
                [0 for i in range(len(self.action_space))])
            actions_array[action] = 1
            print actions_array

            input = np.concatenate((state, actions_array), axis=0)
            reward_before_training = self.model.predict(input.reshape(1, -1))

            reward_after_feedback = reward_before_training
            reward_after_feedback = (1 - self.alpha) * reward_before_training + \
                self.alpha * (reward + self.gamma *
                              self.maxQ_reward(next_state))

            self.model.fit(input.reshape(1, -1),
                           reward_after_feedback, epochs=1, verbose=0)


class Agent(object):

    def __init__(self):
        self.action_space = GAME_CONFIG['action_space']
        self.pi = PolicyOfSingleOutput(self.action_space)
        self.prev_action = 0
        self.prev_state = None
        self.random_factor = 0.9
        self.init_ROS()

    def init_ROS(self):
        rospy.init_node('agent_node', anonymous=True)
        self.action_pub = rospy.Publisher('actions_topic', UInt8, queue_size=1)
        rospy.Subscriber('observations_topic',
                         observation_msg, self.select_action)
        self.rate = rospy.Rate(GAME_CONFIG['game_rate'])
        rospy.spin()

    def should_select_random_action(self, probability):
        if self.random_factor > 0.1:
            self.random_factor = self.random_factor - 0.001  # 0.00003
            # print self.random_factor
        random_action = random.random() < probability
        return random_action

    def select_action(self, message):
        if self.should_select_random_action(self.random_factor):
            action = random.choice(self.action_space)
        else:
            action = self.pi.get_action(message.observation)

        reward = message.reward
        # print reward
        current_state = message.observation

        self.pi.train(self.prev_state, self.prev_action, reward, current_state)

        if not message.isDone:
            self.action_pub.publish(action)

        self.prev_state = current_state
        self.prev_action = action

if __name__ == '__main__':
    agent = Agent()
