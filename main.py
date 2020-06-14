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
from machine import ADC
from dth import DTH
from machine import Pin
from onewire import DS18X20
from onewire import OneWire

adc = ADC()
apin = adc.channel(pin='P16', attn=ADC.ATTN_11DB)
  
def reading():
   avg = 0
   _AVG_NUM = const(100)
   for _ in range (_AVG_NUM):
       avg += apin()
   avg /= _AVG_NUM
   return(avg)

while True:
    analog_val = reading()
    print(analog_val)
    time.sleep(1)
    pass


pwm = PWM(0,frequency = 200)
pwm_c = pwm.channel(0, pin = 'P11', duty_cycle = 0)

while True:
      result = th.read()  
      if result.is_valid():
         pycom.rgbled(0x001000) # green
         print("Temperature: %d C" % result.temperature)
         print("Humidity: %d %%" % result.humidity)
         time.sleep(0.1)

         

  