import gym
import numpy as np
import sys
import copy
import random
import math
from gym import spaces, error


class CrazyFlieBaseEnv(gym.Env):

    # lets say we have 5 actions (hover, left, right, forward, back)
    class Actions(IntEnum):
        left = 0
        right = 1
        forward = 2
        back = 3
        hover = 4


    def __init__(self, seed=None):

        # Action enumeration for this environment
        self.actions = CrazyFlieBaseEnv.Actions

        # Actions are discrete integer values
        self.action_space = spaces.Discrete(len(self.actions))

        #### write code for connecting to the crazyflie using radio ###
        self.reset()

    def reset(self):

        #maybe reset will hover the drone to a fixed z

        obs = None

        return obs



    def step(self, action):



        done = False
        reward = 0
        obs = None


        if action == self.actions.left:
            # write code to move drone to left
            pass

        if action == self.actions.right:
            # write code to move drone to right
            pass




        return obs, reward, done, {}
