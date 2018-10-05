import Adafruit_ADS1x15
from time import sleep, strftime, time
import RPi.GPIO as GPIO
import numpy

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)



adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1

pinLed = 16
GPIO.setup(pinLed, GPIO.OUT)

# collect/read ldr sensor value wit ADS1115

def ldr():
    ldrValue = adc.read_adc(0, gain=GAIN)
    return ldrValue

while True:
	try:
		print('LDR raw value: ' + str(ldr()))
                sleep(2)	
	except KeyboardInterrupt:
                GPIO.cleanup()
                sleep(1)
