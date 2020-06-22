import lora
import struct
import math
import time
import read_dth
import read_photo_resistor
import read_moisture
import read_water
from machine import ADC
from machine import Pin
import _thread

lora.connect_lora()
from lora import s

def send_value():
    try:
        photoRes = read_photo_resistor.value()
         
        soilMoisture = read_moisture.value() #DAC Reference voltage
        waterLevel = read_water.value()
        dth_T, dth_RH = read_dth.value()
        
        #   VMA303 Water and Soil Moisture Module
        #   - Indoor use only.
        #   - Keep away from rain, moisture, splashing and dripping liquids.
        #   - Soil moisture and the water level sensor need to be divided by 10 for correct values.
        
        print('Water level %d ' % waterLevel)
        print('Soil moisture %d ' % soilMoisture)
        
        #   Photoresistor 
        #   - When illuminating photoresist, its resistance changes and with this the current in the circuit changes.    
        #   - Measuring the voltage of the resistance
        #   - Note that the light to voltage ratio is not linear and cannot be used for accurate measurements of brightness.
        #   - Always verify with the voltimeter

        print('Photoresistor (mv): %d' % photoRes)
        
        #   DHT11
        # - Combined sensor that measures both temperature and humidity. 
        # - The sensor is calibrated and needs only an external pullup resistance of ~ 5khm.            
        
        print('dth temp:  %0.2f ' % dth_T)
        print("RH: %0.2f" % dth_RH)
        
        #Packing and sending the data, with focus on optimization
        
        package = (
                   struct.pack('>H',int( (photoRes) * (65536/4096) )) +
                   struct.pack('>H',int( (soilMoisture) * (65536/4096) ))  +
                   struct.pack('>H',int( (waterLevel) * (65536/4096) )) +
                   struct.pack('>B',int( (dth_T+40) * (256/125) )) +
                   struct.pack('>B',int( (dth_RH) * (256/100) )) 
                   ) 
        print('Package', package)
        s.send(package)
    except (NameError, ValueError, TypeError) as e:
        print('Error', e)
        pass
    
    

def interval_(t_):
    while True:
        send_value()
        time.sleep(5)
    

_thread.start_new_thread(interval_,[30])