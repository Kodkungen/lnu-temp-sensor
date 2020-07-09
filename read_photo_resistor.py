

import time
from machine import ADC
from machine import Pin

#ADC READING

adc = ADC()
apin = adc.channel(pin = 'P16', attn = ADC.ATTN_11DB) 

def value():
    analog_val = apin()
    print("Phoresistor %d" % analog_val)
    return (analog_val/16)