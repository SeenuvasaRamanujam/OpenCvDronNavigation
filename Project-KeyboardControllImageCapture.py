from djitellopy import tello
import KeyPressModule as kp
import time
import cv2

me = tello.Tello()
me.connect()
print(me.get_battery())
global img

me.streamon()


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

    if kp.getKey('r'):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img) 
        time.sleep(1)

    return [lr, fb, ud, yv]

while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360,240))
    cv2.inshow("Image, img")
    cv2.waitKey(1) #1milli second
    