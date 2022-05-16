import cv2

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

size= (frameHeight, frameWidth)

cap.set(10, 150) #
result = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc(*'MJPG'),15,size)

while True:
    success, img = cap.read()
    cv2.imshow('Result', img)
    result.write(img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break