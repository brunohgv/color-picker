import numpy as np
import cv2


def showValue(x):
    print(x)


img = np.zeros((300, 500, 3), np.uint8)
cv2.namedWindow('Color Picker')

cv2.createTrackbar('R', 'Color Picker', 0, 255, showValue)
cv2.createTrackbar('G', 'Color Picker', 0, 255, showValue)
cv2.createTrackbar('B', 'Color Picker', 0, 255, showValue)

while 1:
    cv2.imshow('Color Picker', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    b = cv2.getTrackbarPos('B', 'Color Picker')
    g = cv2.getTrackbarPos('G', 'Color Picker')
    r = cv2.getTrackbarPos('R', 'Color Picker')

    img[:] = [b, g, r]

cv2.destroyAllWindows()
