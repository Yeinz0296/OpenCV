import RPi.GPIO as GPIO
import time

Tracking_Left1 = 13   #X1B Left 1 IR sensor
Tracking_Left2 = 15   #X2B Left 2 IR sensor
Tracking_Right1 = 11   #X1A  Right 1 IR sensor
Tracking_Right2 = 7  #X2A  Right 2 IR sensor

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.setup(Tracking_Left1,GPIO.IN)
GPIO.setup(Tracking_Left2,GPIO.IN)
GPIO.setup(Tracking_Right1,GPIO.IN)
GPIO.setup(Tracking_Right2,GPIO.IN)

print ('start')

try:
    while True:
        Tracking_Left1Value = GPIO.input(Tracking_Left1);
        Tracking_Left2Value = GPIO.input(Tracking_Left2);
        Tracking_Right1Value = GPIO.input(Tracking_Right1);
        Tracking_Right2Value = GPIO.input(Tracking_Right2);
        print (Tracking_Left1Value)
        print (Tracking_Left2Value)
        print (Tracking_Right1Value)
        print (Tracking_Right2Value)
        print ('---')
        time.sleep(1)
except KeyboardInterrupt:
    pass
print("Ending")
GPIO.cleanup()