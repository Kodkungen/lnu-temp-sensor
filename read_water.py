import time
from machine import ADC
from machine import Pin

adc = ADC()
apin = adc.channel(pin = 'P14', attn = ADC.ATTN_11DB) 
apin_2 = adc.channel(pin = 'P18', attn = ADC.ATTN_11DB)
apin_3 = adc.channel(pin = 'P19', attn = ADC.ATTN_11DB)

def waterPlantOne():
    plantOne_val = apin()
    print("WaterOne %d" % plantOne_val)
    return (plantOne_val/16)

def waterPlantTwo():
    plantTwo_val = apin_2()
    print("WaterTwo %d" % plantTwo_val)
    return (plantTwo_val/16)

def waterPlantThree():
    plantThree_val = apin_3()
    print("WaterThree %d" % plantThree_val)
    return (plantThree_val/16)

