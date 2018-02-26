#!/usr/bin/env python

import game
import rospy
from std_msgs.msg import String

class Policy(object):
    def __init__(self, action_space):
        self.action_space = action_space

class Agent(object):
    def __init__(self, game):
        self.game = game
        #rospy.init_node('agent', anonymous=True)
        rospy.Subscriber('observations_topic', String, self.callback)

    def callback(self, data):
        print data


if __name__ == '__main__':
    game = game.Enduro()
    agent = Agent(game)
    for i_episode in range(20):
        game.reset()
        for t in range(1000):
            game.run()
            if game.isDone:
                break