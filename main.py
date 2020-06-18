import lora
import struct
import time
import read_dth

lora.connect_lora()
from lora import s

def send_value():
    dth_T, dth_RH = read_dth.value()
    print('dth temp', dth_T)
    print('RH', dth_RH)
    package = struct.pack('>h', int(dth_T)) + struct.pack('>h', int(dth_RH))
    s.send(package)
    
    

while True:
    send_value()
    time.sleep(30)