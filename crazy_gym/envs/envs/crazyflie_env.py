import gym
import numpy as np
import sys
import copy
import random
import math
from enum import Enum
from gym import spaces, error



class CrazyFlieBaseEnv(gym.Env):

    # lets say we have 5 actions (hover, left, right, forward, back)
    class Actions(Enum):
            left = 0
            right = 1
            forward = 2
            back = 3
            hover = 4
            
        # left = 0
        # right = 1
        # forward = 2
        # back = 3
        # hover = 4


    def __init__(self, seed=None):

        # Action enumeration for this environment
        self.actions = CrazyFlieBaseEnv.Actions

        # Actions are discrete integer values
        self.action_space = spaces.Discrete(len(self.actions))

        #### write code for connecting to the crazyflie using radio ###
        import logging
        import sys
        import time

        import cflib.crtp
        from cflib.crazyflie import Crazyflie
        from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
        from cflib.positioning.motion_commander import MotionCommander
        from cflib.utils import uri_helper
        from cflib.utils.multiranger import Multiranger

        #Radio address
        URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')
        self.reset()

        if len(sys.argv) > 1:
            URI = sys.argv[1]

        # Only output errors from the logging framework
        logging.basicConfig(level=logging.ERROR)

    def reset(self):

        #maybe reset will hover the drone to a fixed z
        mc.stop()
        obs = None

        return obs


    def step(self, action):



        done = False
        reward = 0
        obs = None

        cf = Crazyflie(rw_cache='./cache')
        with SyncCrazyflie(URI, cf=cf) as scf:
        # A Crazyflie instance is created and is now connected. If the connection failes,
        # an exception is raised.
        # The MotionCommander is intended to simplify basic autonomous flight,
        # We take off when the commander is created
            with MotionCommander(scf) as motion_commander:
                with Multiranger(scf) as multiranger:
                    keep_flying = True

                    while keep_flying:
                        VELOCITY = 0.5
                        velocity_x = 0.0
                        velocity_y = 0.0

                        # if action == self.actions.left:
                        if action == self.actions.left:
                            
                        # write code to move drone to left
                            velocity_x -= VELOCITY

                        if action == self.actions.right:
                            print("right")
                            velocity_x -= VELOCITY
                            # write code to move drone to right
                            

                        if action == self.actions.front:
                            
                        # write code to move drone to left
                            velocity_y += VELOCITY

                        if action == self.actions.back:
                            
                        # write code to move drone to left
                            velocity_y -= VELOCITY
        return obs, reward, done, {}


