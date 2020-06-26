def value():
    pycom.rgbled(0xFF0000)  # Red
    time.sleep(0.1)
    pycom.rgbled(0x00FF00)  # Green
    time.sleep(0.1)
    pycom.rgbled(0x0000FF)  # Blue
    pwm_c.duty_cycle(0.5)
    time.sleep(0.1)
    pwm_c.duty_cycle(0)