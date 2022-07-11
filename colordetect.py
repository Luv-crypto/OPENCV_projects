import cv2
import string
from math import floor
import numpy as np


def empty(a):
    # print(a)
    pass


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for row_num in range(0, rows):
            for col_num in range(0, cols):
                if imgArray[row_num][col_num].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[row_num][col_num] = cv2.resize(
                        imgArray[row_num][col_num], (0, 0), None, scale, scale
                    )
                else:
                    imgArray[row_num][col_num] = cv2.resize(
                        imgArray[row_num][col_num],
                        (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                        None,
                        scale,
                        scale,
                    )
                if len(imgArray[row_num][col_num].shape) == 2:
                    imgArray[row_num][col_num] = cv2.cvtColor(
                        imgArray[row_num][col_num], cv2.COLOR_GRAY2BGR
                    )
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for row_num in range(0, rows):
            hor[row_num] = np.hstack(imgArray[row_num])
        ver = np.vstack(hor)
    else:
        for row_num in range(0, rows):
            if imgArray[row_num].shape[:2] == imgArray[0].shape[:2]:
                imgArray[row_num] = cv2.resize(
                    imgArray[row_num], (0, 0), None, scale, scale
                )
            else:
                imgArray[row_num] = cv2.resize(
                    imgArray[row_num],
                    (imgArray[0].shape[1], imgArray[0].shape[0]),
                    None,
                    scale,
                    scale,
                )
            if len(imgArray[row_num].shape) == 2:
                imgArray[row_num] = cv2.cvtColor(imgArray[row_num], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


path = "Lambo.png"

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 400, 400)

cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

cv2.createTrackbar("Scale", "TrackBars", 50, 100, empty)


img = cv2.imread(path)

scale = 0.5


while True:
    scale = cv2.getTrackbarPos("Scale", "TrackBars")
    scale /= 100

    scaled_img_size = (floor(scale * img.shape[1]), floor(scale * img.shape[0]))
    imgresized = cv2.resize(img, scaled_img_size)
    imghsv = cv2.cvtColor(imgresized, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imghsv, lower, upper)
    imgResult = cv2.bitwise_and(imgresized, imgresized, mask=mask)
    # cv2.imshow("original", img)
    cv2.imshow("Resized", imgresized)
    cv2.imshow("HSV", imghsv)
    cv2.imshow("MASK", mask)
    cv2.imshow("RESULT", imgResult)

    imgstack = stackImages(0.5, ([imgresized, imghsv], [mask, imgResult]))
    cv2.imshow("STACKEEEEEE", imgstack)

    if cv2.waitKey(50) & 0xFF in {ord(x) for x in string.ascii_letters}:
        break
