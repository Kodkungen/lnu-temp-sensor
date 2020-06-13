#!/usr/bin/env python
#
# Copyright (c) 2019, Pycom Limited.
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing
#

import time
import pycom
import machine
from machine import PWM
from dth import DTH
from machine import Pin
from onewire import DS18X20
from onewire import OneWire

pycom.heartbeat(False)
pycom.rgbled(0x000008) # blue
th = DTH(Pin('P3', mode=Pin.OPEN_DRAIN),0)
pycom.rgbled(0x00FF00)  # Green
time.sleep(0.5)

pwm = PWM(0,frequency = 200)
pwm_c = pwm.channel(0, pin = 'P11', duty_cycle = 0)

while True:
      result = th.read()  
      if result.is_valid():
         pycom.rgbled(0x001000) # green
         print("Temperature: %d C" % result.temperature)
         print("Humidity: %d %%" % result.humidity)
         time.sleep(0.1)
  