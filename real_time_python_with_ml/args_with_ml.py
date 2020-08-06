#!/usr/bin/python
import numpy as np
import pyautogui
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
import serial_with_ml
import time
import joblib
import warnings

warnings.filterwarnings('ignore')

# Load model and preprocessing objects
model = joblib.load(r'sav_files/finalized_model.sav')
scaler = joblib.load(r'sav_files/scaler.sav')
pca_data = joblib.load(r'sav_files/pca.sav')
label_encoder = joblib.load(r'sav_files/label_encoder.sav')

# enter your computer's sensotile port
address= '/dev/cu.usbmodemFFFFFFFEFFFF1'
baud_rate = 9600
timeout = 2
Tsample = 0.01

# serial initialization
sensortile = serial_with_ml.serial_SensorTile(address, baud_rate, timeout, True)

sensortile.init_connection()

def PerformMyGesture(label, confidence):
    if label == "W":
        return
    if confidence < 0.75:
        return

    screen_width, screen_height = pyautogui.size()
    new_x, new_y = pyautogui.position()

    if label == "S":
        pyautogui.click(new_x, new_y)
        return

    if label == "L":
        new_x = new_x - 50
    elif label == "R":
        new_x = new_x + 50
    elif label == "U":
        new_y = new_y - 50
    elif label == "D":
        new_y = new_y + 50

    new_x = max(0, min(screen_width, new_x))
    new_y = max(0, min(screen_height, new_y))

    pyautogui.moveTo(new_x, new_y, duration = 0.25)

while True:
    X_mg,Y_mg,Z_mg,X_mGa,Y_mGa,Z_mGa,X_dps,Y_dps,Z_dps=sensortile.collect_data()

    data = np.array([[np.mean(X_dps), np.mean(X_mGa),np.mean(X_mg),
                      np.mean(Y_dps), np.mean(Y_mGa),np.mean(Y_mg ),
                      np.mean(Z_dps), np.mean(Z_mGa), np.mean(Z_mg )]])

    if not any([np.isnan(val) for val in data[0]]):
        X_scaled = scaler.transform(data)
        X_pca = pca_data.transform(X_scaled)

        ypred = model.predict(X_pca)
        yconf = model.predict_proba(X_pca)
        # get the right label form the model to show the user the predictions and then use the
        # function to control the mouse with the predicted movement 
        label = label_encoder.inverse_transform(ypred)
        print('Predcited gesture = {} | {}'.format(label, np.max(yconf)))
        PerformMyGesture(label[0], np.max(yconf))

# shutdown the system after closing the plot
sensortile.close_connection()
