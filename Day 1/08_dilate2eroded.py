import cv2
import numpy as np
 
img = cv2.imread('cat.png')
kernel = np.ones((5,5), np.uint8)

imgCanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow('Eroded Image', imgEroded)
cv2.waitKey(0)