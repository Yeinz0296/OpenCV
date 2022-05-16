import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread('Day_2/01_QR_Code/QR.png')

for barcode in decode(img):
    print(barcode.data)
