import RPi.GPIO as GPIO
import time

#Set the pin coding mode to BOARD coding mode
GPIO.setmode(GPIO.BOARD)

#Ignore warning
GPIO.setwarnings(False)

LED1 = 40   #Define the pin of LED1 (red)
LED2 = 38   #Define the pin of LED1 (blue)

GPIO.setup(LED1,GPIO.OUT)
GPIO.setup(LED2,GPIO.OUT)

GPIO.output(LED1, GPIO.HIGH)
GPIO.output(LED2, GPIO.HIGH)

GPIO.output(LED1, GPIO.LOW)
GPIO.output(LED2, GPIO.LOW)

