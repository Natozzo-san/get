import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setup(leds, GPIO.OUT)
for i in range(3):
        for led in leds:
            GPIO.output(led, 1)
            time.sleep(0.2)
            GPIO.output(led, 0)
GPIO.output(leds, 0)







def dec2bin(value): 
    return [int(bit) for bit in format(value).zfill(8)]

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
try:
    t = float(input())
    while True:
        for i in range(256):
             GPIO.output(dac, i)
             time.sleep(t/(256*4))

finally:    
    GPIO.output(dac, 0)
    GPIO.cleanup()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
levels = 2**8
maxU = 3.3
bits = 8

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dec2bin(value): 
    return [int(bit) for bit in bin(value)[2:].zfill(bits)]

def num2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac, signal)
    return signal
def adc():
    for i in range(256):
        GPIO.output(dac, dec2bin(i))
        time.sleep(0.01)
        if GPIO.input(comp) == 0:
            return i
    

try:
    while(True):
        i = adc()
        if i != 0:
            print(i, int(3.3 * i/256 *100)/100, 'v')
finally:
        GPIO.output(dac, 0)
        GPIO.cleanup()

