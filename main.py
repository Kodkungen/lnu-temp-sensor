import lora
import struct
import time
import read_dth
import _thread

lora.connect_lora()
from lora import s

def send_value():
    try:
        dth_T, dth_RH = read_dth.value()
        print('dth temp:  %0.2f ' % dth_T)
        print("RH: %0.2f" % dth_RH) 
        package = (struct.pack('>B',int( (dth_T+40)* (256/125) ) ) +
                   struct.pack('>B',int( (dth_RH)* (256/100) ) ))
        print('Package', package)
        s.send(package)
    except (NameError, ValueError, TypeError):
        pass
    
    

def interval_(t_):
    while True:
        send_value()
        time.sleep(30)
    

_thread.start_new_thread(interval_,[30])