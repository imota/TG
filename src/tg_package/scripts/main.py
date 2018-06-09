#!/usr/bin/env python

import environments
import json
import pandas as pd
from std_msgs.msg import String
from tg_package.msg import observation_msg


if __name__ == '__main__':
    game = environments.get_game()

    for i_episode in range(10):
        print 'Episode: ' + str(i_episode)
        game.reset()
        while not game.isDone:
            game.run()

        episode_number = 'Episode ' + str(i_episode + 1)

        with open('results_enduro_random.csv', 'a') as f:
            reward = game.get_cummulative_reward()
            d = {'Episode': [episode_number], 'Reward': [reward]}
            df = pd.DataFrame(data=d)
            df.to_csv(f, header=False)
