# Taken from https://github.com/iot-lnu/applied-iot-20/tree/master/sensor-examples

import time
from machine import ADC
from machine import Pin

""" For testing

# voltage = (apin.voltage() + apin.voltage() + apin.voltage() + apin.voltage()) / 4
  print("VOLT moisture plant A %d " % voltage) """

adc = ADC()
apin = adc.channel(pin = 'P15', attn = ADC.ATTN_11DB)
apin_plantTwo = adc.channel(pin = 'P13', attn = ADC.ATTN_11DB)
apin_plantThree = adc.channel(pin = 'P17', attn = ADC.ATTN_11DB)

def moisturePlantOne():
    plantOne_val = apin()
    print("moistPlantOne %d" % plantOne_val)
    return (plantOne_val/16)

def moisturePlantTwo():
   plantTwo_val = apin_plantTwo()
   print("moistPlantTwo %d" % plantTwo_val)
   return (plantTwo_val/16)

def moisturePlantThree():
   plantThree_val = apin_plantThree()
   print("moistPlantThree %d" % plantThree_val)
   return (plantThree_val/16)