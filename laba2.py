import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD )
GPIO.setup(3 , GPIO.OUT )
GPIO.setup(5, GPIO.IN)
#GPIO.output(3 , 1 )
while True:
    GPIO.output(3,GPIO.input(5))


