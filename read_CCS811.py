# Example for CCS811 sensor, Taken from https://github.com/iot-lnu/applied-iot-20/tree/master/sensor-examples

from machine import I2C
import time

i2c = I2C(0)                         # create on bus 0
i2c = I2C(0, I2C.MASTER)             # create and init as a master
i2c = I2C(0, pins=('P9','P10'))      # PIN assignments (P9=SDA, P10=SCL)
i2c.init(I2C.MASTER, baudrate=10000) # init as a master

# https://github.com/Notthemarsian/CCS811

import CCS811
ccs = CCS811.CCS811(i2c=i2c,addr=91)
time.sleep(3) # Otherwise we get false readings


def value():
    ccs.data_ready() # Make a reading
    co2 = ccs.eCO2
    voc = ccs.tVOC
    print("Co2 %d" % co2)
    print("Voc %d" % voc)
    if co2 > 399:    # Filter out faulty readings
        return(co2,voc)
        