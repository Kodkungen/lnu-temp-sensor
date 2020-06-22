#Get values from the water & moisture sensor

#När man belyser fotoresistor, förändras dess resistans och med detta förändras strömmen i kretsen. Spänningen på resistansen.

import time
from machine import ADC
from machine import Pin

adc = ADC()
apin = adc.channel(pin = 'P14', attn = ADC.ATTN_11DB) 

def value():
    analog_val = apin()
    #print("Phoresistor %d" % analog_val)
    return analog_val