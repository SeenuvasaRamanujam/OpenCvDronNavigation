from djitellopy import tello
import KeyPressModule as kp
from time import sleep


kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery)

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 10

    if kp.getkey("LEFT"): lr = -speed
    elif kp.getkey("RIGHT"): lr = speed

    if kp.getkey("w"): fb = speed
    elif kp.getkey("s"): fb = -speed

    if kp.getkey("UP"): ud = speed
    elif kp.getkey("DOWN"): ud = -speed

    if kp.getkey("a"): yv = -speed
    elif kp.getkey("d"): yv = speed

    if kp.getkey("q"): ud = me.land
    elif kp.getkey("e"): ud = me.takeoff   
    
    return [lr, fb, ud, yv]

while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.1)

