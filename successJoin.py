import time
from machine import Pin,  PWM

def value():

    # Define frequency for the tones
    G6  = 1568
    E7  = 2637
    G7  = 3136
    C7  = 2093

    # set up pin PWM timer for output to buzzer or speaker
    buz = Pin("P11") # Pin Y2 with timer 8 Channel 2
    tim = PWM(0, frequency=300)
    ch = tim.channel(2, duty_cycle=0.5, pin=buz)

    marioSound = [E7, E7, 0, E7, 0, C7, E7, 0, G7, 0, 0, 0, G6, 0, 0, 0]

    for i in marioSound:
        if i == 0:
            ch.duty_cycle(0)
        else:
            tim=PWM(0, frequency=i)  # changes frequency for each tone
            ch.duty_cycle(0.50)
        time.sleep(0.150)
        duty_cycle = 0