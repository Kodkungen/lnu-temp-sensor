import time
from machine import ADC
from machine import Pin

adc = ADC()
apin = adc.channel(pin = 'P15', attn = ADC.ATTN_11DB)
apin_plantTwo = adc.channel(pin = 'P13', attn = ADC.ATTN_11DB)
apin_plantThree = adc.channel(pin = 'P17', attn = ADC.ATTN_11DB)

def moisturePlantOne():
    plantOne_val = apin()
    print("moistPlantOne %d" % plantOne_val)
    return plantOne_val

def moisturePlantTwo():
   plantTwo_val = apin_plantTwo()
   print("moistPlantTwo %d" % plantTwo_val)
   return plantTwo_val

def moisturePlantThree():
   plantThree_val = apin_plantThree()
   print("moistPlantThree %d" % plantThree_val)
   return plantThree_val