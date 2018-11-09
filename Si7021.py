import board
import busio
import adafruit_si7021
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_si7021.SI7021(i2c)

print('Temperature: {0:0.2f} degrees C'.format(sensor.temperature))
print('Humidity: {0:0.2f}%'.format(sensor.relative_humidity))
