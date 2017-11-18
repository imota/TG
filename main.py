import gym

environments = ['MsPacman-v0', 'Enduro-v0', 'CartPole-v0']

env = gym.make(environments[0])
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break