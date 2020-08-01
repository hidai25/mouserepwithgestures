# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 10:47:10 2020
@author: Hidai Bar-Mor
"""

#!/usr/bin/python


import numpy as np

import pyautogui


import Nina_serial_hidai


import time



address= '/dev/cu.usbmodemFFFFFFFEFFFF1'

baud_rate = 9600

timeout = 2

Tsample = 0.01


# serial initialization

sensortile = Nina_serial_hidai.serial_SensorTile(address, baud_rate, timeout, True)

sensortile.init_connection()

x, y = pyautogui.position()

screen_width, screen_height = pyautogui.size()

while True:

    accelx, accely, accelz, gyrx, gyry, gyrz, magx, magy, magz = sensortile.collect_data()
    #Hidai needs to add angular velocity, accelaration, and whatever is used by the model
    accelx = list(accelx)
    accely = list(accely)
    accelz = list(accelz)
    gyrx = list(gyrx)
    gyry = list(gyry)
    gyrz = list(gyrz)
    magx = list(magx)
    magy = list(magy)
    magz = list(magz)

    time.sleep(1)

    if len(accelx) > 0:
        print('ACCEL_x = ', sum(accelx)/len(accelx))
    if len(accely) > 0:
        print('ACCEL_y = ', sum(accely)/len(accely))
    if len(accelz) > 0:
        print('ACCEL_z = ', sum(accelz)/len(accelz))

    if len(gyrx) > 0:
        print('GYR_x = ', sum(gyrx)/len(gyrx))
    if len(gyry) > 0:
        print('GYR_y = ', sum(gyry)/len(gyry))
    if len(gyrz) > 0:
        print('GYR_z = ', sum(gyrz)/len(gyrz))

    if len(magx) > 0:
        print('MAG_x = ', sum(magx)/len(magx))
    if len(magy) > 0:
        print('MAG_y = ', sum(magy)/len(magy))
    if len(magz) > 0:
        print('MAG_z = ', sum(magz)/len(magz))


    #this is where Vikram needs to insert his code (create a vector of accelaration, displcement, ...)
    #prediction, confidence = model(short_history_displ, short_history_accel, ...)

    #if confidence > 0.8 and prediction == "L":
    #   pyautogui.moveTo(current_x - 10, current_y, duration = 0.25)
    current_x, current_y = pyautogui.position()
    new_x = current_x
    new_y = current_y
    if len(accelx) > 0:
        delta_x = sum(accelx)/len(accelx)
        if np.abs(delta_x) > 50:
            new_x -= delta_x
    if len(accely) > 0:
        delta_y = sum(accely)/len(accely)
        if np.abs(delta_y) > 50:
            new_y -= delta_y

    new_x = max(0, min(screen_width, new_x))
    new_y = max(0, min(screen_height, new_y))

   # pyautogui.moveTo(new_x, new_y, duration = 0.25)

# shutdown the system after closing the plot

sensortile.close_connection()
