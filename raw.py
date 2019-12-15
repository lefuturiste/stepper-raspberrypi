from gpiozero import DigitalOutputDevice
import time

step = DigitalOutputDevice(27)
dir = DigitalOutputDevice(17)

i = 0

dir.value = True

while True:
   i = 0
   while i < 200:
      step.value = True
      time.sleep(0.001)
      step.value = False
      time.sleep(0.001)
   
   print('Full', i)
