from gpiozero import DigitalOutputDevice
import time
import math

class Stepper:
    def __init__(self, dirPin, stepPin, sleepPin = None):
        self.dir =  DigitalOutputDevice(dirPin)
        self.step = DigitalOutputDevice(stepPin)
        if sleepPin != None:
            self.enableOutput = DigitalOutputDevice(sleepPin)    
            # by default we disable the card
            self.disable()
        else: 
            # if no enable pin is provided we consider the device as always enabled
            self.enableOutput = None
            self.enabled = True
        self.value = 0
        self.scale = 2 * math.pi
        self.minSpeed = 0.002
        self.maxSpeed = 0.0005
        
    def setScale(self, scale):
        self.scale = scale
        
    '''
    Referencial for clockwise and anticlockwise
    when the stepper motor pinout is pointed at the top
    '''
    def setClockwise(self):
        self.dir.value = False
        
    def setAnticlockwise(self):
        self.dir.value = True
        
    def getPosition(self):
        return (self.scale*self.value)/200
        
    '''
    Speed: 1 = Max speeed; 0 = Min speed
    '''
    def move(self, steps, speed = 0.5):
        interstice = self.maxSpeed + (abs(self.minSpeed - self.maxSpeed) * (1-speed))
        #0.0005+(math.abs(0.0005-0.002)*0.5)
        print(interstice)
        for i in range(steps):
            self.value += 1
            self.step.value = True
            time.sleep(interstice)
            self.step.value = False
            time.sleep(interstice)
    
    def fullRotation(self):
        self.move(200)
    
    def enable(self):
        if self.enableOutput != None:
            self.enableOutput.value = False
            self.enabled = True
        
    def disable(self):
        if self.enableOutput != None:
            self.enableOutput.value = True
            self.enabled = False