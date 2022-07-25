from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery())

me.takeoff()
me.send_rc_control(0, 50, 0, 0) #move left or rigth, move forward or backward, for up or down, rotation of yaw
sleep(2)
me.send_rc_control(0, 0, 0, 0) #for landing
me.land()