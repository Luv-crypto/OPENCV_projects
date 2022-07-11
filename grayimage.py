import cv2
import os
import numpy as np

kernel = np.ones((5, 5), np.uint8)
# Moving to file directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

img = cv2.imread("ideation.jpeg")

imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgblur = cv2.GaussianBlur(imggray, (3, 3), 0)
imgcanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgcanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)
cv2.imshow("Gray Image", imggray)
cv2.imshow("Blur Image", imgblur)
cv2.imshow("Canny Image", imgcanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)
