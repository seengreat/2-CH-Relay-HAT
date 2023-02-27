# Seengreat 2-ch Relay HAT demo
# Author(s):Andy Li from Seengreat

import os
import sys
import time
import wiringpi as wpi

"""the following pin definiting use wiringpi"""
PIN_CH1     = 25
PIN_CH2     = 24

STATE_ON    = wpi.LOW
STATE_OFF   = wpi.HIGH

class RELAY_2CH():
    def __init__(self):
        # gpio init
        wpi.wiringPiSetup()
        wpi.pinMode(PIN_CH1, wpi.OUTPUT)  # CH1 pin
        wpi.pinMode(PIN_CH2, wpi.OUTPUT)  # CH2 pin
        wpi.digitalWrite(PIN_CH1, STATE_OFF)
        wpi.digitalWrite(PIN_CH2, STATE_OFF)
    def control(self, ch, state):
        if ch == 1:
            wpi.digitalWrite(PIN_CH1, state)
        elif ch == 2: 
            wpi.digitalWrite(PIN_CH2, state)
if __name__ == '__main__':
    relay = RELAY_2CH()
    while True:
        print("ch1 relay on")
        relay.control(1, STATE_ON)
        time.sleep(1)
        print("ch1 relay off")
        relay.control(1, STATE_OFF)
        print("ch2 relay on")
        relay.control(2, STATE_ON)
        time.sleep(1)
        print("ch2 relay off")
        relay.control(2, STATE_OFF)
