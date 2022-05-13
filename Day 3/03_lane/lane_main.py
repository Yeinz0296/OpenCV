#from MotorModule import Motor
import cv2
import YB_Pcb_Car
from lane_tracking import getLaneCurve
import webcam_module

car = YB_Pcb_Car.YB_Pcb_Car()
car.Ctrl_Servo(1,93)
car.Ctrl_Servo(2,160)

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
    car.Ctrl_Car(0.20,-curveVal*sen,0.05)
    #cv2.waitKey(1)
     
 
if __name__ == '__main__':
    while True:
        main()