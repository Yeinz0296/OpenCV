import cv2
from cv2 import waitKey

frameWidth = 480
frameHeight = 240

cap = cv2.VideoCapture("TestVideo.mp4")
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)

while True:
    success, img = cap.read() #To check if it success or not
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

