#!/usr/bin/env python
#Installation reference on windows: https://towardsdatascience.com/how-to-install-openai-gym-in-a-windows-environment-338969e24d30

import environments
import json
import pandas as pd
from datetime import datetime

def write_results(episode_number):
    pass

if __name__ == '__main__':
    print('Starting program...')
    game = environments.get_game()

    num_episodes = 1
    for i_episode in range(1):
        print('Starting episode: ' + str(i_episode + 1))
        start_time = datetime.now()
        game.play()    
        game_time = datetime.now() - start_time
        write_results(i_episode + 1)
    print('End of program')