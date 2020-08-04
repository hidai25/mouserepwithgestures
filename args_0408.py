# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 11:38:51 2020

@author: Hidai Bar-Mor
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 10:47:10 2020
@author: Hidai Bar-Mor
"""

#!/usr/bin/python


import numpy as np

import pyautogui

import pandas as pd

from sklearn.preprocessing import StandardScaler, LabelEncoder


import serial_0408

import time

import joblib

# Load model and preprocessing objects
model = joblib.load(r'sav_files/finalized_model.sav')
scaler = joblib.load(r'sav_files/scaler.sav')
pca_data = joblib.load(r'sav_files/pca.sav')
tsne = joblib.load(r'sav_files/tsne.sav')
label_encoder = joblib.load(r'sav_files/label_encoder.sav')


address= 'COM4'

baud_rate = 9600

timeout = 2

Tsample = 0.01


# serial initialization

sensortile = serial_0408.serial_SensorTile(address, baud_rate, timeout, True)

sensortile.init_connection()

x, y = pyautogui.position()

screen_width, screen_height = pyautogui.size()

while True:
  
   
   X_mg,Y_mg,Z_mg,X_mGa,Y_mGa,Z_mGa,X_dps,Y_dps,Z_dps=sensortile.collect_data()
   
   data = np.array([[np.mean(X_dps), np.mean(X_mGa),np.mean(X_mg),
                 np.mean(Y_dps), np.mean(Y_mGa),np.mean(Y_mg ),
                 np.mean(Z_dps), np.mean(Z_mGa), np.mean(Z_mg )]])
   
   [print(idx) for idx,val in enumerate(data[0]) if np.isnan(val)]
   
   if not any([np.isnan(val) for val in data[0]]):
       
       X_scaled = scaler.fit_transform(data)
       X_pca = pca_data.fit(X_scaled)
       X_tsne = tsne.transform(X_pca)
       
       ypred = model.predict(X_tsne)
       
       label = label_encoder.inverse_transform(ypred)
       
       print('Predcited gesture = ', label)

        


    
       




       
       

  
    
  
    
  
    
    #this is where Vikram needs to insert his code (create a vector of accelaration, displcement, ...)
    #prediction, confidence = model(short_history_displ, short_history_accel, ...)
    
    #if confidence > 0.8 and prediction == "L":
    #   pyautogui.moveTo(current_x - 10, current_y, duration = 0.25)
 #   current_x, current_y = pyautogui.position()
  #  new_x = current_x
  #  new_y = current_y
 #   if len(accelx) > 0:
 #       delta_x = sum(accelx)/len(accelx)
 #       if np.abs(delta_x) > 50:
 #           new_x -= delta_x
 #   if len(accely) > 0:
 #       delta_y = sum(accely)/len(accely)
##        if np.abs(delta_y) > 50:
#            new_y -= delta_y

 #   new_x = max(0, min(screen_width, new_x))
 #   new_y = max(0, min(screen_height, new_y))

    #pyautogui.moveTo(new_x, new_y, duration = 0.25)

# shutdown the system after closing the plot

sensortile.close_connection()
