#Get values from the water & moisture sensor

""" import time
from machine import ADC
from machine import Pin

adc = ADC()
apin = adc.channel(pin = 'P16', attn = ADC.ATTN_11DB)

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
    pass """