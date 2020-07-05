import time
from machine import ADC
from machine import Pin

adc = ADC()
apin = adc.channel(pin = 'P14', attn = ADC.ATTN_11DB) 
apin_2 = adc.channel(pin = 'P18', attn = ADC.ATTN_11DB)
apin_3 = adc.channel(pin = 'P19', attn = ADC.ATTN_11DB)

def waterPlantOne():
    plantOne_val = apin()
    #print("Phoresistor %d" % analog_val)
    return plantOne_val

def waterPlantTwo():
    plantTwo_val = apin_2()
    return plantTwo_val

def waterPlantThree():
    plantThree_val = apin_3()
    return plantThree_val

