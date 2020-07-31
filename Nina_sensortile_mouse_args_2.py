

# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 10:47:10 2020

@author: Hidai Bar-Mor
"""

#!/usr/bin/python

import datetime as dt

#import matplotlib; matplotlib.use("TkAgg")

#import matplotlib.pyplot as plt

#import matplotlib.animation as animation

import numpy as np

import pyautogui

#import SensorTile_Serial

import Nina_serial_hidai

import sys

import time





address= '/dev/cu.usbmodemFFFFFFFEFFFF1'

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

sensortile = Nina_serial_hidai.serial_SensorTile(address, baud_rate, timeout, True)

sensortile.init_connection()

x, y = pyautogui.position()
velx = [0]
vely = [0]
displx = [x]
disply = [y]
screen_width, screen_height = pyautogui.size()

while True:
    velx = [velx[-1]]
    vely = [vely[-1]]
    displx = [displx[-1]]
    disply = [disply[-1]]
    accelx, accely, accelz = sensortile.collect_data()
    #Hidai needs to add angular velocity, accelaration, and whatever is used by the model
    accelx = list(accelx)
    accely = list(accely)
    time.sleep(1)
    for i in range(len(accelx)-1): # perpform Forward Euler step
        velx.append(velx[-1]+Tsample*(accelx[i]+accelx[i+1])/2)
        displx.append(displx[-1]+Tsample*velx[-1])
    if len(accelx) > 0:
        print('ACCEL_x = ', sum(accelx)/len(accelx))
    if len(accely) > 0:
        print('ACCEL_y = ', sum(accely)/len(accely))
    print('DISPLx = ' , sum(displx)/len(displx))
    print('DISPLy = ' , sum(disply)/len(disply))
    
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

    pyautogui.moveTo(new_x, new_y, duration = 0.25)

# shutdown the system after closing the plot

sensortile.close_connection()
