import cv2
import numpy as np

img = cv2.imread("road.png")
print(img.shape) #To print the current image size #(Height, Width, BGR)

width, height = 640, 480 #Can resize to small and big
imgResize = cv2.resize(img,(width,height))
print(imgResize.shape)

imgCropped = imgResize[250:480,0:640] #[Start Point height:end point height, start point width:end point width]

#cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)