from dth import DTH
from machine import Pin
import time

# Type 0 = dht11
# Type 1 = dht22

th = DTH(Pin('P3', mode=Pin.OPEN_DRAIN), 0)
time.sleep(1)

def value():
    result = th.read()
    if result.is_valid(): return(result.temperature,result.humidity)