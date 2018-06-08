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

    def __init__(self, input_size=(6)):
        super(Net, self).__init__()
        self.learning_rate = 0.1

        self.fc1 = nn.Linear(input_size, 2)
        self.fc2 = nn.Linear(2, 5)
        self.fc3 = nn.Linear(5, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return F.log_softmax(x)


class PolicyOfSingleOutput(object):

    def __init__(self, action_space):
        self.action_space = action_space
        self.gamma = 0.618
        self.alpha = 0.9
        self.state_size = GAME_CONFIG['state_size']

        self.net = Net()

        self.optimizer = torch.optim.SGD(
            self.net.parameters(), lr=self.net.learning_rate, momentum=0.9)
        self.criterion = nn.KLDivLoss()

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
            input = Variable(torch.Tensor(input))
            #input = input.view(-1, 6)

            self.optimizer.zero_grad()

            reward_before_training = self.net(input)

            reward_after_feedback = reward_before_training
            reward_after_feedback = (1 - self.alpha) * reward_before_training + \
                self.alpha * (reward + self.gamma *
                              self.maxQ_reward(next_state))

            out = Variable(reward_before_training, requires_grad=True)
            target = Variable(reward_after_feedback)
            loss = self.criterion(out, target)
            print out, target
            loss.backward()
            self.optimizer.step()


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
            action = self.pi.get_best_action(message.observation)

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
