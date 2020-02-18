#!/usr/bin/env python
#Installation reference on windows: https://towardsdatascience.com/how-to-install-openai-gym-in-a-windows-environment-338969e24d30

import environments
import json
import pandas as pd

def write_results(episode_number):
#    episode_number = 'Episode ' + str(i_episode)

#    with open('results_pacman_sincrono.csv', 'a') as f:
#        reward = game.get_cummulative_reward()
#        d = {'Episode': [episode_number], 'Reward': [reward]}
#        df = pd.DataFrame(data=d)
#        df.to_csv(f, header=False)   
    pass

if __name__ == '__main__':
    print('Starting program...')
    game = environments.get_game()

    # with open('results_pinball_random.csv', 'a') as f:
    #    d = {'Episode', 'Reward'}
    #    df = pd.DataFrame(data=d)
    #    df.to_csv(f, header=False)

    num_episodes = 1
    for i_episode in range(1):
        print('Starting episode: ' + str(i_episode + 1))
        game.play()    
        write_results(i_episode + 1)
    print('End of program')