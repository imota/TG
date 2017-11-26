import gym

class Game:
    def prepare(self, environment_name):
        self.environment = environment_name
        self.env = gym.make(self.environment)
        self.isDone = False
        self.reset()      

    def reset(self):
        self.observation = self.env.reset()

    def select_action(self):
        return self.env.action_space.sample()

    def run(self):
        self.env.render()
        action = self.select_action()
        observation, reward, done, info = self.env.step(action)

        self.observation = observation
        self.isDone = done

class Enduro(Game):
    def __init__(self):
        self.prepare('Enduro-v0')

class MsPacman(Game):
    def __init__(self):
        self.prepare('MsPacman-v0')

class CartPole(Game):
    def __init__(self):
        self.prepare('CartPole-v0')