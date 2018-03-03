#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt8


class Policy(object):

    def __init__(self, action_space):
        self.action_space = action_space


class Agent(object):

    def __init__(self):
        rospy.init_node('agent_node', anonymous=True)
        self.action_pub = rospy.Publisher(
            'actions_topic', UInt8, queue_size=1)
        rospy.Subscriber('observations_topic', String, self.callback)
        self.rate = rospy.Rate(10)
        rospy.spin()

    def callback(self, data):
        self.action_pub.publish(2)

if __name__ == '__main__':
    agent = Agent()
