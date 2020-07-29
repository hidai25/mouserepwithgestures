# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:31:28 2020

@author: Hidai Bar-Mor
"""

#!/usr/bin/python


import pyautogui


import serial_test2


import autopy




address= 'COM4'

baud_rate = 9600

timeout = 2

Tsample = 0.01

def mov_avg(mylist, N):
    cumsum, moving_aves = [0], []

    for i, x in enumerate(mylist, 1):
        cumsum.append(cumsum[i-1] + x)
        if i>=N:
            moving_ave = (cumsum[i] - cumsum[i-N])/N
            #can do stuff with moving_ave here
            moving_aves.append(moving_ave)
    return moving_aves



# serial initialization

sensortile = serial_test2.serial_SensorTile(address, baud_rate, timeout, True)

sensortile.init_connection()

x, y = pyautogui.position()
bias_displ = 0
posxs = []
posys = []
while True:

    accelx, accely = sensortile.collect_data()

    #time.sleep(0.5)
    if len(accelx) > 0:
        print('ACCELx = ', sum(accelx)/len(accelx))
        print('ACCELy = ', sum(accely)/len(accely))


    if len(accelx) > 0:
        avg_accelx = sum(accelx)/len(accelx)
        avg_accely = sum(accely)/len(accely)

        scale = autopy.screen.scale()
        autopy.mouse.move(abs(avg_accelx) /scale,(abs((avg_accely) /scale)-500))

    size_x, size_y = pyautogui.size() # 683, 384



# shutdown the system after closing the plot

sensortile.close_connection()
