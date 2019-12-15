from Stepper import Stepper
from math import degrees
from time import sleep

stepper = Stepper(17, 27, 22)
stepper.setClockwise()
stepper.enable()
stepper.move(100, 0.5)
stepper.disable()
print(degrees(stepper.getPosition()) % 360)

while True:
    sleep(1)
