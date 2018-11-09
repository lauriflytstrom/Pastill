import RPi.GPIO as GPIO

import board 

import busio
i2c = busio.I2C(board.SCL, board.SDA)

import time

import adafruit_tsl2561
sensor0 = adafruit_tsl2561.TSL2561(i2c)

import adafruit_si7021
sensor1 = adafruit_si7021.SI7021(i2c)

import Adafruit_BMP.BMP085 as BMP085
sensor2 = BMP085.BMP085()



while True:
    
            
    print('Lux: {}'.format(sensor0.lux))
    print('Broadband: {}'.format(sensor0.broadband))
    print('Infrared: {}'.format(sensor0.infrared))
    print('Luminosity: {}'.format(sensor0.luminosity))
    #print('Temperature: {} degrees C'.format(sensor1.temperature))
    print('Humidity: {}%'.format(sensor1.relative_humidity))
    print ('Temp = {0:0.2f} *C'.format(sensor2.read_temperature())) 
    print ('Pressure = {0:0.2f} Pa'.format(sensor2.read_pressure())) 
    #print ('Altitude = {0:0.2f} m'.format(sensor2.read_altitude())) 
    #print ('Sealevel Pressure = {0:0.2f} Pa'.format(sensor2.read_sealevel_pressure())) 

    
    GPIO.setwarnings(False)
    pins=[21,20,16,12,7,8,25,24,23,4,17,27,22,10,9,11]

    for pin in pins:
        GPIO.setup(pin,GPIO.OUT)

    temp=int(round(sensor2.read_temperature()))
    
    for num in range(len(pins)):
        if num+15 <= temp:
            GPIO.output(pins[num],1)
        if num+15 > temp:
            GPIO.output(pins[num],0)

    time.sleep(5)
