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
from machine import PWM
from machine import Pin
from onewire import DS18X20
from onewire import OneWire

pycom.heartbeat(False)

pwm = PWM(0,frequency = 200)
pwm_c = pwm.channel(0, pin = 'P11', duty_cycle = 0)
#DS18B20 data line connected to pin P21
ow = OneWire(Pin('P10'))
temp = DS18X20(ow)

while True:
    temp_reading = temp.read_temp_async()

    if temp_reading != None:
      if temp_reading < 30:
        pycom.rgbled(0x7f7f00 + int (temp_reading*200))
        print(temp_reading)
    temp.start_conversion()
    time.sleep(1)


    pycom.rgbled(0xFF0000)  # Red
    time.sleep(0.1)
    pycom.rgbled(0x00FF00)  # Green
    time.sleep(0.1)
    pycom.rgbled(0x0000FF)  # Blue
    pwm_c.duty_cycle(0.5)
    time.sleep(0.1)
    pwm_c.duty_cycle(0)

    