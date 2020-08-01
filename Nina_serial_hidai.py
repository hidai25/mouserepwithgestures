# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 21:06:33 2020
@author: Hidai Bar-Mor
"""

import serial

import time

import re
pattern = 'ACC_X: (\S?[0-9]+), ACC_Y: (\S?[0-9]+), ACC_Z: (\S?[0-9]+)' #mac needs comma
prog = re.compile(pattern)
pattern1 = 'GYR_X: (\S?[0-9]+), GYR_Y: (\S?[0-9]+), GYR_Z: (\S?[0-9]+)'
prog1 = re.compile(pattern1)
pattern2 = 'MAG_X: (\S?[0-9]+), MAG_Y: (\S?[0-9]+), MAG_Z: (\S?[0-9]+)'
prog2 = re.compile(pattern2)

class serial_SensorTile():

    def __init__(self, address, baud_rate=9600, timeout=2, python3=False):

        self.ser = None

        self.last_line = ""

        # serial information

        self.address = address

        self.baud_rate = baud_rate

        self.timeout = timeout

        # flag

        self.data_check = 0

        self.python3 = python3



    def init_connection(self):

        print ("Start Serial Connection")


        ser = serial.Serial(self.address, self.baud_rate, timeout=self.timeout)

        self.ser = ser

        # sleep 500ms before accepting data

        time.sleep(0.5)

        self.ser.flushInput()



    def close_connection(self):

        print ("Close Serial Connection")

        self.ser.close()



    def is_ready(self, bytes_expected):

        return self.ser.in_waiting >= bytes_expected



    def collect_data(self):

        accelx = []
        accely = []
        accelz = []
        gyrx = []
        gyry = []
        gyrz = []
        magx = []
        magy = []
        magz = []


        if self.data_check:

            # read all new bytes

            bytesToRead = self.ser.in_waiting

            ser_bytes = self.ser.read(bytesToRead)

            # convert byte to string python 3

            if self.python3:

                ser_bytes = ser_bytes.decode("utf-8")

            ser_bytes = self.last_line + ser_bytes  # prepend previous unfinished line

            ser_bytes = ser_bytes.split('\n')       # split lines

            self.last_line = ser_bytes[-1]          # save unfinished line

            ser_bytes = ser_bytes[0:-1]             # discard unfinished line




            for line in ser_bytes:

                # discard \r

                line = line.rstrip()

                # split data

                data = line.split('\t')



                if 'ACC' in data[0]:
                    print("{}".format(data[0].replace("\r","")))

                    result = prog.findall(data[0].replace("\r",""))[0]

                    accelx.append(float(result[0]))
                    accely.append(float(result[1]))
                    accelz.append(float(result[2]))

                if 'GYR' in data[0]:
                    print("{}".format(data[0].replace("\r","")))

                    result1 = prog1.findall(data[0].replace("\r",""))[0]

                    gyrx.append(float(result1[0]))
                    gyry.append(float(result1[1]))
                    gyrz.append(float(result1[2]))


                if 'MAG' in data[0]:
                    print("{}".format(data[0].replace("\r","")))

                    result2 = prog2.findall(data[0].replace("\r",""))[0]

                    magx.append(float(result2[0]))
                    magy.append(float(result2[1]))
                    magz.append(float(result2[2]))


            return accelx, accely, accelz, gyrx, gyry, gyrz, magx, magy, magz

        else:

            # discard the first corrupted line

            self.ser.reset_input_buffer()

            self.ser.readline()

            self.data_check = 1

            return accelx, accely, accelz, gyrx, gyry, gyrz, magx, magy, magz
