#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 14:10:22 2020

@author: hidaibar-mor
"""

from __future__ import print_function
import usb1

def hotplug_callback(context, device, event):
    print("Device %s: %s" % (
        {
            usb1.HOTPLUG_EVENT_DEVICE_ARRIVED: 'arrived',
            usb1.HOTPLUG_EVENT_DEVICE_LEFT: 'left',
        }[event],
        device,
    ))
    
def main():
    with usb1.USBContext() as context:
        if not context.hasCapability(usb1.CAP_HAS_HOTPLUG):
            print('Hotplug support is missing. Please update your libusb version.')
            return
        print('Registering hotplug callback...')
        opaque = context.hotplugRegisterCallback(hotplug_callback)
        print('Callback registered. Monitoring events, ^C to exit')
        try:
            while True:
                context.handleEvents()
        except (KeyboardInterrupt, SystemExit):
            print('Exiting')

if __name__ == '__main__':
    main()
