"""
Scenario:
1 dealer, n players playing blackjack
"""


import numpy as np
from multiagent.core import World, Agent, Landmark
from multiagent.scenario import BaseScenario
import random

class Dealer(Agent):
    def __init__(self):
        super(Dealer, self).__init__()

class Player(Agent):
    def __init__(self):
        super(Player, self).__init__()

class Scenario(BaseScenario):

    def make_world(self):
        pass

    def reset_world(self, world):
        pass

    def reward(self, agent, world):
        pass

    def observation(self, agent, world):
        pass