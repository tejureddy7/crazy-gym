'''
This examples uses the Flow and Multi-ranger decks to move in all directions 
'''
import gym
import numpy as np
import sys
import copy
import random
import math

from gym import spaces, error
from enum import IntEnum
import logging
import sys
import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.utils import uri_helper
from cflib.utils.multiranger import Multiranger




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

        #initialize drivers
        cflib.crtp.init_drivers()

        #Radio address
        self.URI = uri_helper.uri_from_env(default='radio://0/70/2M/E7E7E7E702')
        self.reset()

        if len(sys.argv) > 1:
            URI = sys.argv[1]

        # Only output errors from the logging framework
        logging.basicConfig(level=logging.ERROR)

        self.reset()

    def reset(self):

        #maybe reset will hover the drone to a fixed z

        obs = None

        return obs



    def step(self, action):



        done = False
        reward = 0
        obs = None
        cf = Crazyflie(rw_cache='./cache')


        with SyncCrazyflie(self.URI, cf=cf) as scf:
        # A Crazyflie instance is created and is now connected. If the connection failes,
        # an exception is raised.
        # The MotionCommander is intended to simplify basic autonomous flight,
        # We take off when the commander is created
            DEFAULT_HEIGHT = 0.4
            with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as self.mc:
                with Multiranger(scf) as multiranger:
                    keep_flying = True
                    

                    while keep_flying:
                        VELOCITY = 0.5
                        velocity_x = 0.0
                        velocity_y = 0.0
                        print("action", action)
                        print("self.actions.left",self.actions.left)
                        
                        #left
                        if action == self.actions.left:
                            velocity_x -= VELOCITY
                            time.sleep(1)

                        #move right
                        if action == self.actions.right:            
                            velocity_x -= VELOCITY
                            time.sleep(1)
                
                        #move forward   
                        if action == self.actions.forward:
                            velocity_y += VELOCITY
                            time.sleep(1)

                        #move back
                        if action == self.actions.back:            
                            velocity_y -= VELOCITY
                            time.sleep(1)

                        #hover
                        if action == self.actions.hover:            
                            mc.stop()
                            time.sleep(1)

        return obs, reward, done, {}
