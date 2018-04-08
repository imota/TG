#!/usr/bin/env python

import environments
import rospy
from std_msgs.msg import String


if __name__ == '__main__':
    game = environments.get_game()

    for i_episode in range(1000):
        print 'Eisode: ' + str(i_episode)
        game.reset()
        while not game.isDone:
            game.run()
