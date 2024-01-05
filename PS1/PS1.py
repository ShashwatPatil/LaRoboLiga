import gym
import os
import time as t
import LaRoboLiga24
import cv2
import pybullet as p

CAR_LOCATION = [-25.5,0,1.5]


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
    arena = "arena1",
    car_location=CAR_LOCATION,
    visual_cam_settings=VISUAL_CAM_SETTINGS
)


vel=[[0,0],
     [0,0]]
while True:
    p.stepSimulation()
    img = env.get_image(cam_height=0, dims=[600, 600])
    keys = p.getKeyboardEvents()


    if p.B3G_UP_ARROW in keys and keys[p.B3G_UP_ARROW] & p.KEY_IS_DOWN:
        for a in vel:
            a[0] += 0.3
            a[1] += 0.3
        env.move(vels=vel)

    elif p.B3G_LEFT_ARROW in keys and keys[p.B3G_LEFT_ARROW] & p.KEY_IS_DOWN:
        for a in vel:
            a[0] -= 0.1
            a[1] += 0.1
        env.move(vels=vel)

    elif p.B3G_DOWN_ARROW in keys and keys[p.B3G_DOWN_ARROW] & p.KEY_IS_DOWN:
        for a in vel:
            a[0] -= 0.4
            a[1] -= 0.4
        env.move(vels=vel)

    elif p.B3G_RIGHT_ARROW in keys and keys[p.B3G_RIGHT_ARROW] & p.KEY_IS_DOWN:
        for a in vel:
            a[0] += 0.1
            a[1] -= 0.1
        env.move(vels=vel)

    elif 32 in keys and keys[32] & p.KEY_IS_DOWN:
        vel = [[0, 0],
               [0, 0]]
        env.move(vels=vel)
    else:
        pass
    cv2.imshow("image", img)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
env.close()
