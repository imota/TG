#!/usr/bin/env python

import rospy
import random
from std_msgs.msg import String, UInt8
from config import GAME_CONFIG


class Policy(object):

    def __init__(self, action_space):
        self.action_space = action_space


class Agent(object):

    def __init__(self):
        rospy.init_node('agent_node', anonymous=True)
        self.action_pub = rospy.Publisher('actions_topic', UInt8, queue_size=1)
        rospy.Subscriber('observations_topic', String, self.callback)
        self.rate = rospy.Rate(GAME_CONFIG['game_rate'])
        rospy.spin()

    def callback(self, data):
        self.action_pub.publish(random.randint(0, GAME_CONFIG['action_space']))

if __name__ == '__main__':
    agent = Agent()
