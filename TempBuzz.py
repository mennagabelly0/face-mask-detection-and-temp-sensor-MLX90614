import RPi.GPIO as gpio
import time
import smtplib
from smbus2 import SMBus
from mlx90614 import MLX90614

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT) #GPIO PIN 17

while 1:
    bus = SMBus(1)
    sensor = MLX90614(bus, address=0x5A)
    print ("Ambient Temperature :", sensor.get_ambient())
    print( "Object Temperature :", sensor.get_object_1())
    temp = sensor.get_object_1()
    bus.close()
    if temp>37:
        GPIO.output(11, 1)
        time.sleep(0.1)
    else:
        time.sleep(0.01)
