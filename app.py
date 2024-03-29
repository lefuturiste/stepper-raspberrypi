from Stepper import Stepper
from math import degrees
from time import sleep
import sys
import os 

stepper = Stepper(17, 18, 27)

def main():
    while True:
        stepper.setClockwise()
        stepper.enable()
        stepper.move(300, 1)
        print('Stop')
        sleep(0.5)
        print('Replay')
        stepper.setAnticlockwise()
        stepper.move(300, 1)
        #stepper.disable()
        print(degrees(stepper.getPosition()) % 360)
        sleep(1)

    while True:
        sleep(1)

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
