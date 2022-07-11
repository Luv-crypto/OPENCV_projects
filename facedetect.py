import cv2

faseCascade = cv2.CascadeClassifier(
    "Cascades\\frontalFace10\\haarcascade_frontalface_alt.xml"
)

img = cv2.imread("Lenna.png")
imggray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

faces = faseCascade.detectMultiScale(imggray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


cv2.imshow("bot", img)
cv2.waitKey(0)
