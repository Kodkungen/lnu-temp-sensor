import lora
import struct
import math
import time
import read_dth
import read_photo_resistor
import read_moisture
import read_water
import read_CCS811
from machine import ADC
from machine import Pin
import _thread

lora.connect_lora()
from lora import s

time.sleep(2)

def send_value():
    try:
        co2,voc = read_CCS811.value()
        photoRes = read_photo_resistor.value()
               
        soilMoisturePlantOne = read_moisture.moisturePlantOne() #DAC Reference voltage
        soilMoisturePlantTwo = read_moisture.moisturePlantTwo()
        soilMoisturePlantThree = read_moisture.moisturePlantThree()
        
        waterLevelPlantOne = read_water.waterPlantOne() 
        waterLevelPlantTwo = read_water.waterPlantTwo()
        waterlevelPlantThree = read_water.waterPlantThree()
        dth_T, dth_RH = read_dth.value()
    
        
        print('co2 %d' % co2)
        print('voc %d' % voc)
        
        print('Photoresistor (mv): %d' % photoRes)
        
        print('WaterlevelPlantOne %d ' % waterLevelPlantOne)
        print('WaterlevelPlantTwo %d ' % waterLevelPlantTwo)
        print('WaterlevelPlantThree %d ' % waterlevelPlantThree)
        
        
        print('SoilmoisturePlantOne %d' % soilMoisturePlantOne)
        print('SoilMoisturePlantTwo %d' % soilMoisturePlantTwo)
        print('SoilMoisturePlantThree %d' % soilMoisturePlantThree)         
        
        print('dth temp:  %0.2f ' % dth_T)
        print("RH: %0.2f" % dth_RH)
        
        #Packing and sending the data, with focus on optimization
        
        package = (struct.pack('>H',int(co2) ) +
                   struct.pack('>H',int(voc) ) +
                   struct.pack('>H',int( (photoRes) * (65536/4096) )) +
                   struct.pack('>H',int( (soilMoisturePlantOne) * (65536/4096) ))  +
                   struct.pack('>H',int( (soilMoisturePlantTwo) * (65536/4096) )) +
                   struct.pack('>H',int( (soilMoisturePlantThree) * (65536/4096) )) +
                   struct.pack('>H',int( (waterLevelPlantOne) * (65536/4096) )) +
                   struct.pack('>H',int( (waterLevelPlantTwo) * (65536/4096) )) +
                   struct.pack('>H',int( (waterlevelPlantThree) * (65536/4096) )) +
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
        time.sleep(10) #Send value every 10 seconds for calculating electronic energy
    

_thread.start_new_thread(interval_,[30])