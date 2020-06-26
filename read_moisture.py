#Get values from the water & moisture sensor

#När man belyser fotoresistor, förändras dess resistans och med detta förändras strömmen i kretsen. Spänningen på resistansen.

import time
from machine import ADC
from machine import Pin

adc = ADC()
apin = adc.channel(pin = 'P15', attn = ADC.ATTN_11DB)
apin_plantTwo = adc.channel(pin = 'P13', attn = ADC.ATTN_11DB)
apin_plantThree = adc.channel(pin = 'P17', attn = ADC.ATTN_11DB)


def moisturePlantOne():
    plantOne_val = apin()
    #print("Phoresistor %d" % analog_val)
    return plantOne_val

def moisturePlantTwo():
   plantTwo_val = apin_plantTwo()
   return plantTwo_val

def moisturePlantThree():
   plantThree_val = apin_plantThree()
   return plantThree_val