import YB_Pcb_Car
import PID
import cv2

global target_valuex
target_valuex = 2048
global target_valuey
target_valuey = 2048

xservo_pid = PID.PositionalPID(1.1, 0.2, 0.8)
yservo_pid = PID.PositionalPID(0.8, 0.2, 0.8)

car = YB_Pcb_Car.YB_Pcb_Car()
car.Ctrl_Servo(1,90)
car.Ctrl_Servo(2,90)

face_haar = cv2.CascadeClassifier('/home/pi/opencv/data/haarcascades/haarcascade_frontalface_default.xml')

image = cv2.VideoCapture(0)
image.set(3,320) # set Width
image.set(4,240) # set Height
image.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M', 'J', 'P', 'G'))
image.set(cv2.CAP_PROP_BRIGHTNESS, 62) 
image.set(cv2.CAP_PROP_CONTRAST, 63) 
image.set(cv2.CAP_PROP_EXPOSURE, 4800)


while True:
    ret, frame = image.read()
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #faces = face_haar.detectMultiScale(gray_img, 1.1, 3)
    faces = face_haar.detectMultiScale(
        gray_img,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )
    #xservo_pid = PID.PositionalPID(XServo_P.value, XServo_I.value, XServo_D.value)
    #yservo_pid = PID.PositionalPID(YServo_P.value, YServo_I.value, YServo_D.value)

    for (x,y,w,h) in faces:
    #if len(faces)>0:
        #(x, y, w, h) = faces[0]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        #roi_gray = gray_img[y:y+h, x:x+w]
        #roi_color = frame[y:y+h, x:x+w]
        xservo_pid.SystemOutput = x + w/2
        xservo_pid.SetStepSignal(150)
        xservo_pid.SetInertiaTime(0.01, 0.1)
        target_valuex = int(1500 + xservo_pid.SystemOutput)
        target_servox = int((target_valuex-500)/10)
        if target_servox > 180:
            target_servox = 180
        if target_servox < 0:
            target_servox = 0 
        yservo_pid.SystemOutput = y + h/2
        yservo_pid.SetStepSignal(120)
        yservo_pid.SetInertiaTime(0.01, 0.1)
        target_valuey = int(1500 - yservo_pid.SystemOutput)
        target_servoy = int((target_valuey-500)/10)                        
        print("target_servoy %d", target_servoy)
        print("target_servox %d", target_servox)  
        if target_servoy > 180:
            target_servoy = 180
        if target_servoy < 0:
            target_servoy = 0        
        #robot.Servo_control(target_valuex,target_valuey)
            
        car.Ctrl_Servo(1, target_servox)
 
        car.Ctrl_Servo(2, target_servoy)
        
    cv2.imshow('video',frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
    
image.release()
cv2.destroyAllWindows()