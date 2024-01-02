import gym
import os
import time as t
import LaRoboLiga24
import cv2


CAR_LOCATION = [2,3,1.5]
BALL_LOCATION = [4,5,1.5]
HUMANOID_LOCATION = [-3,-4,1.3]
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
    ball_location=BALL_LOCATION,
    humanoid_location=HUMANOID_LOCATION,
    visual_cam_settings=VISUAL_CAM_SETTINGS
)

t.sleep(100)
env.close()
