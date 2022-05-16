#from MotorModule import Motor
import cv2
import YB_Pcb_Car
from lane_tracking import getLaneCurve
import webcam_module
import numpy as np
from time import sleep

car = YB_Pcb_Car.YB_Pcb_Car()
car.Ctrl_Servo(1,93)
car.Ctrl_Servo(2,100)

class Motor():
    
    def move(self,speed=0.5,turn=0,t=0):
        speed *=100
        turn *=70
        leftSpeed = speed-turn
        rightSpeed = speed+turn

        if leftSpeed>100: leftSpeed =100
        elif leftSpeed<-100: leftSpeed = -100
        if rightSpeed>100: rightSpeed =100
        elif rightSpeed<-100: rightSpeed = -100
        #print(leftSpeed,rightSpeed)
        
        if leftSpeed>0:
            car.Car_Left(leftSpeed,rightSpeed)
        else:
            car.Car_Right(leftSpeed,rightSpeed)
        if rightSpeed>0:
            car.Car_Right(leftSpeed,rightSpeed)
        else:
            car.Car_Left(leftSpeed,rightSpeed)
        sleep(t)

def main():

    img = webcam_module.getImg()
    curveVal= getLaneCurve(img,1)
 
    sen = 1.3  # SENSITIVITY
    maxVAl= 0.3 # MAX SPEED
    if curveVal>maxVAl:curveVal = maxVAl
    if curveVal<-maxVAl: curveVal =-maxVAl
    #print(curveVal)
    if curveVal>0:
        sen =1.7
        if curveVal<0.05: curveVal=0
    else:
        if curveVal>-0.08: curveVal=0
        
    Motor.move(0.20,-curveVal*sen,0.05)
    #cv2.waitKey(1)
     
 
if __name__ == '__main__':
    while True:
        main()