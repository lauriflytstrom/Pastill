import Adafruit_BMP.BMP085 as BMP085
sensor = BMP085.BMP085()


import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


pins=[40,38,36,32,26,24,22,18,16,7,11,13,15,19,21,23]

for pin in pins:
    GPIO.setup(pin,GPIO.OUT)

while True:
    temp=int(round(sensor.read_temperature()))
    
    for num in range(len(pins)):
        if num+15 <= temp:
            GPIO.output(pins[num],1)
        if num+15 > temp:
            GPIO.output(pins[num],0)
        
    
   
    #print ('Temp = {0:0.2f} *C'.format(sensor.read_temperature()))
    
    print ('Temp = {} *C'.format(int(round(sensor.read_temperature()))))
    time.sleep(5)
