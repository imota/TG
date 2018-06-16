#!/usr/bin/env python

import rospy
import random
import numpy as np
from std_msgs.msg import UInt8
from config import GAME_CONFIG
from tg_package.msg import observation_msg

import torch

import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable


class Net(nn.Module):

    def __init__(self, input_size, learning_rate):
        super(Net, self).__init__()
        self.learning_rate = learning_rate

        self.fc1 = nn.Linear(input_size, 10)
        self.relu = nn.ReLU()  # POSSIVEL FONTE DE ERRO
        self.fc2 = nn.Linear(10, 5)
        self.fc22 = nn.Linear(300, 1000)
        self.fc23 = nn.Linear(1000, 1000)
        self.fc24 = nn.Linear(1000, 300)
        self.fc3 = nn.Linear(5, 1)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        out = self.relu(out)
        #out = self.fc22(out)
        #out = self.relu(out)
        #out = self.fc23(out)
        #out = self.relu(out)
        #out = self.fc24(out)
        #out = self.relu(out)
        out = self.fc3(out)
        return out


class PolicyOfSingleOutput(object):

    def __init__(self, action_space):
        self.action_space = action_space
        self.gamma = 0.9
        self.alpha = 0.65
        self.state_size = GAME_CONFIG['state_size']

        self.net = Net(input_size=self.get_input_size(), learning_rate=0.5)

        self.optimizer = torch.optim.Adam(
            self.net.parameters(), lr=self.net.learning_rate)
        self.criterion = nn.MSELoss()  # POSSIVEL FONTE DE ERRO

    def get_input_size(self):
        return self.state_size + len(self.action_space)

    def get_best_action(self, state):
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
            input = Variable(torch.Tensor(input))
            reward = self.net(input)
            # print action, reward
            if reward >= max_reward:
                max_action = action
                max_reward = reward
        # print "----"
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

            input = np.concatenate((state, actions_array), axis=0)
            input = Variable(torch.Tensor(input))
            input = input.view(-1, self.get_input_size())

            self.optimizer.zero_grad()

            reward_before_training = self.net(input)

            reward_after_feedback = reward_before_training
            reward_after_feedback = (1 - self.alpha) * reward_before_training + \
                self.alpha * (reward + self.gamma *
                              self.maxQ_reward(next_state))

            out = Variable(reward_before_training, requires_grad=True)
            target = Variable(reward_after_feedback)
            loss = self.criterion(out, target)
            loss.backward()
            self.optimizer.step()


class RandomPolicy(object):

    def __init__(self, action_space):
        self.action_space = action_space

    def get_best_action(self, state):
        return random.choice(self.action_space)

    def train(self, state, action, reward, next_state):
        pass


class Agent(object):

    def __init__(self):
        self.action_space = GAME_CONFIG['action_space']
        self.pi = PolicyOfSingleOutput(self.action_space)
        self.prev_action = 0
        self.prev_state = None
        self.random_probability = 1.0
        self.random_discount_factor = 0.0002  # 0.0005
        self.init_ROS()

    def init_ROS(self):
        rospy.init_node('agent_node', anonymous=True)
        self.action_pub = rospy.Publisher('actions_topic', UInt8, queue_size=1)
        rospy.Subscriber('observations_topic',
                         observation_msg, self.select_action)
        self.rate = rospy.Rate(GAME_CONFIG['game_rate'])
        rospy.spin()

    def should_select_random_action(self, probability):
        return random.random() < probability

    def select_action(self, message):
        if self.should_select_random_action(self.random_probability):
            action = random.choice(self.action_space)
        else:
            action = self.pi.get_best_action(message.observation)

        reward = message.reward
        current_state = message.observation

        self.pi.train(self.prev_state, self.prev_action, reward, current_state)

        if not message.isDone:
            self.action_pub.publish(action)
        else:
            print self.random_probability
            if self.random_probability > 0.05:
                self.random_probability = self.random_probability - self.random_discount_factor

        self.prev_state = current_state
        self.prev_action = action

if __name__ == '__main__':
    agent = Agent()
