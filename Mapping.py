import math
from djitellopy import tello
import KeyPressModule as kp
import time as sleep
import numpy as np
import cv2


########### PARAMETERS ###########
fSpeed = 117/10 #Forward Speed in cm/s (15cm/s)
aSpeed = 360/10 #Angular Speed Degrees/s
interval = 0.5

dInterval = fSpeed*interval
aInterval = aSpeed*interval
####################################
x, y = 500, 500
a = 0
yaw = 0

points = []

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery)

points = [(0,0,), (0,0)]

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    
    speed = 10
    aspeed = 50 
    d = 0
    global x, y, yaw

    if kp.getkey("LEFT"): 
        lr = -speed
        d = dInterval
        a = -180

    elif kp.getkey("RIGHT"): 
        lr = speed
        d = -dInterval
        a = 180

    if kp.getkey("w"):
        fb = speed
        d = dInterval
        a = 270

    elif kp.getkey("s"): 
        fb = -speed
        d = -dInterval
        a = 90

    if kp.getkey("UP"): 
        ud = speed

    elif kp.getkey("DOWN"): 
        ud = -speed
        
    if kp.getkey("a"): 
        yv = -aspeed
        yaw -= aInterval

    elif kp.getkey("d"): 
        yv = aspeed
        yaw += aInterval

    if kp.getkey("q"): 
        me.land(); sleep(3)

    elif kp.getkey("e"): 
        me.takeoff()
    
    sleep(interval)
    a += yaw
    x += int(d*math.cos(math.radians(a)))
    y += int(d*math.sin(math.radians(a)))

    return [lr, fb, ud, yv, x, y]

def drawPoints(img, points):
    for point in points:
        cv2.circle(img, points, 10, (0,0,255), cv2.FILLED) #BGR
    cv2.putText(img, f'({(points[-1][0] - 500) / 100},{(points[-1][1] - 500) / 100})m',
    (points[-1][0] + 10, points[-1][1] + 30), cv2.FONT_HERSHEY_PLAIN,1,(255,0,255), 1)



while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    img = np.zeros((1000, 1000, 3), np.uint8)
    if (points[-1][0] != vals[4] or points[-1][1] != vals[5]):
        points.append((vals[4], vals[5]))
    drawPoints(img, points)
    cv2.imshow("Output", img)
    cv2.waitKey(1)


    #text mmm
