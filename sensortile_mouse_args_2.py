

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

import serial_hidai

import sys

import time





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

sensortile = serial_hidai.serial_SensorTile(address, baud_rate, timeout, True)

sensortile.init_connection()

x, y = pyautogui.position()
velx = [0]
vely = [0]
displx = [x]
disply = [y]
while True:
    velx = [velx[-1]]
    vely = [vely[-1]]
    displx = [displx[-1]]
    disply = [disply[-1]]
    accelx, accely, accelz = sensortile.collect_data()
    accelx = [x for x in accelx]
    #accelx = mov_avg(accelx,5)
    for i in range(len(accelx)-1): # perpform Forward Euler step
        velx.append(velx[-1]+Tsample*(accelx[i]+accelx[i+1])/2)
        displx.append(displx[-1]+Tsample*velx[-1])
    time.sleep(1)
    if len(accelx) > 0:
        print('ACCEL = ', sum(accelx)/len(accelx))
    #print('VEL = ' , sum(velx)/len(velx))
    print('DISPLx = ' , sum(displx)/len(displx))
    print('DISPLy = ' , sum(disply)/len(disply))
    meandisplx = sum(displx)/len(displx)
    meandisply = sum(disply)/len(disply)
    pyautogui.moveTo(meandisplx, meandisply)



# This function is called periodically from pyautogui library

# def control_mouse(i, xs, ys):


def control_mouse(i, ys1, ys2):



    # get  acceleration,gyroscope data

    acc_list, gyr_list = sensortile.collect_data()



    # Add acc and gyr to lists

    ys1.extend(acc_list)

    ys2.extend(gyr_list)

    x_len = 200

    # Limit x and y lists to 200 samples - 2s

    ys1 = ys1[-x_len:]

    ys2 = ys2[-x_len:]

#ax1.set_ylim(dis_range)

#line1, = ax1.plot(xs, ys1, animated=True)

#ax2.set_ylim(accel_range)

#line2, = ax2.plot(xs, ys2, animated=True)

    move1= pyautogui.moveRel(30,0)
    move2= pyautogui.moveRel(0,30)

    # Draw acc and gyr lists

    move1.set_ydata(ys1)

    move2.set_ydata(ys2)



    return move1, move2



# Set up plot to call pyautogui function periodically

interval = 10





# shutdown the system after closing the plot

sensortile.close_connection()
