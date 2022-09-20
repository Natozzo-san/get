import RPi.GPIO as GPIO
import time
import random
GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [1, 1, 0, 1, 0, 1, 0, 1]
GPIO.setup(dac, GPIO.OUT)
for i in range(8):
    number[i] = random.randrange(0, 2)
    print(number[i])
GPIO.output(dac, number)
time.sleep(1)
GPIO.output(dac, 0)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
number = [1, 1, 1, 1, 1, 1, 1, 1]
GPIO.output(dac, number)
time.sleep(5)
GPIO.output(dac, 0)