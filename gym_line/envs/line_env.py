import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym.spaces import Box

import random
import math


class LineEnv(gym.Env):
    metadata = {'render.modes': ['ansi']}

    def __init__(self):
        super(LineEnv, self).__init__()
        self.high = 50
        self.action_space = Box(low=-1 * self.high, high=self.high, shape=(1,))
        self.observation_space = Box(
            low=-1 * self.high, high=self.high, shape=(1,))

    def _reset(self):

        self.x = self.observation_space.sample()
        self.history = [self.x]
        return [self.x]

    def _step(self, action):
        if len(self.history) > 200:
            return [self.x], 0.0, True, None
        self.jitter = random.random()
        self.x = self.x + action[0] + self.jitter * 2
        if self.x < -1 * self.high:
            self.x = -1 * self.high
        elif self.x > self.high:
            self.x = self.high
        self.history.append(self.x)
        return [self.x], -math.fabs(self.x) - math.pow(action[0] * .5, 2), False, None

    def _render(self, mode='human', close=False):
        if mode == 'ansi':
            return str(self.x)
        else:
            raise Exception("Not supported")
