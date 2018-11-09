# Pastill


## Raspberry pi sensor setup (BMP180, Si7021, TSL2561) and LED thermometer

With BMP180 and multi LEDs you can see temperature in one °C accuracy in LEDs and more accuracy in python3 shell. You also get more data when you connect Si7021 and TSL2561 to your raspberry pi. 

First you need to check that your raspberry pi has 40 GPIO Pins  because the LED setup is made for 40 pins and doesn't work in 26 pins. Then you need to check that your raspberry is using python 3 and you have raspbian newest version(Rasbian GNU/Linux 9.4 stretch) installed in your raspberry (check it using by code `sudo apt-get update` and `sudo apt-get upgrade`

Then you can start connecting sensors and LEDs to GPIO pins by following these instructions:

1. First you need to connect sensors in the way that this picture shows (you can connect all sensors in same ports):
![Alt](/images/sensor_setup.png "Sensor setup")

2. Then you need to connect LEDs longer parts to GPIO pins in this way:

| GPIO Pins     | Leds (left to right) |
| ------------- |--------------------- |
| 40            | 1                    |
| 38            | 2                    |
| 36            | 3                    |
| 32            | 4                    |
| 26            | 5                    |
| 24            | 6                    |
| 22            | 7                    |
| 18            | 8                    |
| 16            | 9                    |
| 7             | 10                   |
| 11            | 11                   |
| 13            | 12                   |
| 15            | 13                   |
| 29            | 14                   |
| 31            | 15                   |
| 33            | 16                   |

3. Then you need connect LEDs other parts together and then with one cable to pin 39 (GND).


Then you need to enable [I2C](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c) and [SPI](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-spi) and instructions are in links.

Once you're done with both and have rebooted, verify you have the I2C and SPI devices with the command
```
ls /dev/i2c* /dev/spi*
```

You should see the response
```
/dev/i2c-1 /dev/spidev0.0 /dev/spidev0.1
```

Then you need to install some libraries by using these codes:
```
sudo apt-get install git build-essential python-dev python-smbus
git clone https://github.com/adafruit/Adafruit_Python_BMP.git
cd Adafruit_Python_BMP
sudo python setup.py install
cd
mkdir ~/BMP180Code
cd ~/BMP180Code 
sudo pip3 install --upgrade setuptools
pip3 install adafruit-blinka
sudo pip3 install adafruit-circuitpython-tsl2561
sudo pip3 install adafruit-circuitpython-si7021
```

Then you can just load python3 code from [this link](https://github.com/lauriflytstrom/Pastill) and then you can run it with:
```
python3 <filename.py>
```

## Links
https://thepihut.com/blogs/raspberry-pi-tutorials/18025084-sensors-pressure-temperature-and-altitude-with-the-bmp180

https://learn.adafruit.com/tsl2561/python-circuitpython

https://learn.adafruit.com/adafruit-si7021-temperature-plus-humidity-sensor/circuitpython-code

https://maker.pro/raspberry-pi/tutorial/how-to-interface-a-pir-motion-sensor-with-raspberry-pi-gpio







