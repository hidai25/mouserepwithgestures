#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 14:44:27 2020

@author: hidaibar-mor
"""


import pyautogui, sys


#im1 = pyautogui.screenshot(region=(100,100, 150, 180))
#im2 = pyautogui.screenshot('my_screenshot.png')
size=pyautogui.size()
print(size)

position=pyautogui.position()

print(position)




#try:
#    while True:
 #       x, y = pyautogui.position()
  #      positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
   #     print(positionStr, end='')
    #    print('\b' * len(positionStr), end='', flush=True)
#except KeyboardInterrupt:
 #   print('\n')



#pyautogui.moveTo(100, 200, 2)
#pyautogui.click(x=236, y=27)


#pyautogui.click(button='right')

#pyautogui.click(clicks=2)


#pyautogui.click(button='right', clicks=3, interval=0.25)

#pyautogui.doubleClick()

#pyautogui.tripleClick()



pyautogui.scroll(10)   # scroll up 10 "clicks"
pyautogui.scroll(-10)  # scroll down 10 "clicks"
pyautogui.scroll(10, x=100, y=100)

pyautogui.mouseDown();
pyautogui.mouseUp()  # does the same thing as a left-button mouse click
pyautogui.mouseDown(button='right')  # press the right button down
pyautogui.mouseUp(button='right', x=100, y=200)
