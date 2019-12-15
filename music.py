
from Stepper import Stepper
from math import degrees
from time import sleep
from gpiozero import DigitalInputDevice
from threading import Thread
from curtsies import Input
import sys
import os 


stepper = Stepper(17, 27, 22)
stepper.setClockwise()
btn = DigitalInputDevice(23, True)

def watchInput():
    global speed
    with Input(keynames='curses') as input_generator:
        for e in input_generator:
            print(speed)
            if e == 'KEY_UP':
                if speed < 1.3:
                    speed += 0.01
            if e == 'KEY_DOWN':
                if speed-0.01 > 0:
                    speed -= 0.01
            if e == 'KEY_RIGHT':
                if stepper.isClockwise:
                    stepper.setAnticlockwise()
                else:
                    stepper.setClockwise()

speed = 0.01
dirAndSpeedThread = Thread(target=watchInput)
dirAndSpeedThread.start()

def main():
    while True:
        if btn.value: 
            while btn.value:
                stepper.enable()
                stepper.move(1, speed)
                stepper.disable()
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        stepper.disable()
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)