import gym
import os
import time as t
import LaRoboLiga24
import cv2


CAR_LOCATION = [-5,0,1.5]

BALLS_LOCATION = dict({
    'red'    : [3,4,1.5],
    'blue' : [4,-3,1.5],
    'yellow'   : [2,1,1.5],
    'green' : [3,-2,1.5]
})

HUMANOIDS_LOCATION = dict({
    'red'    : [11,1.5,0.8],
    'blue' : [-11,-1.5,0.8],
    'yellow'   : [-1.5,11,8],
    'green' : [-1.5,-11,8]
})

VISUAL_CAM_SETTINGS = dict({
    'cam_dist'       : 13,
    'cam_yaw'        : 0,
    'cam_pitch'      : -110,
    'cam_target_pos' : [0,4,0]
})

################################################################
"""
change the values you pass in arena to the values to load diff arenas 
arena = "default", "arena1", "arena2"
"""
################################################################

os.chdir(os.path.dirname(os.getcwd()))
env = gym.make('LaRoboLiga24',
    arena = "arena2",
    car_location=CAR_LOCATION,
    ball_location=BALLS_LOCATION,
    humanoid_location=HUMANOIDS_LOCATION,
    visual_cam_settings=VISUAL_CAM_SETTINGS
)

t.sleep(100)
env.close()
