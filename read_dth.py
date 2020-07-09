# Taken from https://github.com/iot-lnu/applied-iot-20/tree/master/sensor-examples

from dth import DTH
from machine import Pin
import time

# Type 0 = dht11 - used right now
# Type 1 = dht22

th = DTH(Pin('P3', mode=Pin.OPEN_DRAIN), 0)
time.sleep(3)

def value():    
    result = th.read()
    print("Temperature: %d C" % result.temperature)	
    print("Humidity: %d" % result.humidity)
    if result.is_valid():
         return(result.temperature,result.humidity)