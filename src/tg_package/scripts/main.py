#!/usr/bin/env python

import environments
import json
import pandas as pd
from std_msgs.msg import String
from tg_package.msg import observation_msg


if __name__ == '__main__':
    game = environments.get_game()

    # with open('results_pinball_random.csv', 'a') as f:
    #    d = {'Episode', 'Reward'}
    #    df = pd.DataFrame(data=d)
    #    df.to_csv(f, header=False)

    for i_episode in range(5000):
        print 'Episode: ' + str(i_episode)
        game.reset()
        game.game_step()
        while not game.isDone:
            game.run()

        episode_number = 'Episode ' + str(i_episode + 1)

        with open('results_pacman_sincrono.csv', 'a') as f:
            reward = game.get_cummulative_reward()
            d = {'Episode': [episode_number], 'Reward': [reward]}
            df = pd.DataFrame(data=d)
            df.to_csv(f, header=False)
