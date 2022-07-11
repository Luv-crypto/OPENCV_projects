import cv2
import numpy as np

img = cv2.imread("Lambo.png")
imgResized = cv2.resize(img, (500, 279))
imgcropped = img[0:200, 300:600]
print(img.shape)
cv2.imshow("image", img)
cv2.imshow("imageresized", imgResized)
cv2.imshow("imgCropped", imgcropped)
cv2.waitKey(0)
