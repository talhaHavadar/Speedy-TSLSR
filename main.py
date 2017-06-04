import cv2
import numpy as np
import matplotlib.pyplot as plt
from tslsr import tslsr, utils
import glob

image = cv2.imread("../../images/speed-2.jpg", 1)
mask, circles, rois = tslsr.tslsr(image)
plt.figure(1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

if len(rois) > 0:

    plt.figure(2)
    plt.subplot(221)
    roi = cv2.cvtColor(rois[0], cv2.COLOR_BGR2RGB)
    plt.imshow(roi)

    plt.subplot(224)
    roi_hsv = cv2.cvtColor(roi, cv2.COLOR_RGB2HSV)
    plt.imshow(roi_hsv, cmap="hsv")

    mroi, rects = tslsr.__bound_contours(roi)
    digits = tslsr.extractDigits(roi)

    plt.subplot(222)
    plt.imshow(mroi)

    croi = roi.copy()
    for (x, y, w, h) in utils.eliminate_child_rects(rects):
        cv2.rectangle(croi, (x, y), (x+w, y+h), (0, 255, 0), 1)

    plt.subplot(223)
    plt.imshow(croi)

    plt.figure(3)

    recognizedDigits = []

    for digit in digits:
        res = tslsr.recognizeDigit(digit)
        print("Recoginition res:", res)
        recognizedDigits.append(res[0])

    for i in range(len(digits)):
        p = int("1" + str(len(digits)) + "" + str(i + 1))
        digit = digits[i].copy()
        digit = cv2.cvtColor(digit, cv2.COLOR_BGR2GRAY)
        ret, digit = cv2.threshold(digit, 90, 255, cv2.THRESH_BINARY_INV)
        plt.subplot(p)
        plt.title("Digit recognized as " + str(recognizedDigits[i]))
        plt.imshow(digit, cmap="gray")

plt.show()
