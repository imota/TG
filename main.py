#!/usr/bin/env python

import environments
import rospy
from std_msgs.msg import String


if __name__ == '__main__':
    game = environments.Enduro()

    for i_episode in range(20):
        game.reset()
        for t in range(1000):
            game.run()
            if game.isDone:
                break
