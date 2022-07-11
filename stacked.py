import cv2
import numpy as np


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


img = cv2.imread("ideation.jpeg")
staimages = stackImages(0.4, ([img, img, img], [img, img, img]))
# imgresi = cv2.resize(img, (200, 200))
# imghor = np.hstack((imgresi, imgresi))
# imgver = np.vstack((imgresi, imgresi))
# cv2.imshow("Horizontal", imghor)
# cv2.imshow("vertical", imgver)
cv2.imshow("stackes", staimages)
cv2.waitKey(0)
