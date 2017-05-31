import cv2
import numpy as np
import matplotlib.pyplot as plt
from tslsr import tslsr

image = cv2.imread("../../images/speed-1.jpg", 1)
mask, circles, rois = tslsr.tslsr(image)

plt.figure(1)
plt.subplot(221)
roi = cv2.cvtColor(rois[0], cv2.COLOR_BGR2RGB)
plt.imshow(roi.copy())

plt.subplot(222)
roi_hsv = cv2.cvtColor(roi, cv2.COLOR_RGB2HSV)

mask1 = cv2.inRange(roi_hsv, np.array([0, 0, 0]), np.array([180, 255, 50]))
mask1 = cv2.morphologyEx(mask1, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)))
mask1 = cv2.GaussianBlur(mask1, (5, 5), 0)
mask1 = cv2.Canny(mask1, 100, 200)
mask1 = cv2.morphologyEx(mask1, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
plt.imshow(mask1, cmap="gray")

im2, cnts, hierarchy = cv2.findContours(mask1.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]

for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    x, y, w, h = cv2.boundingRect(approx)
    print("ApproxLen:", len(approx), "rect:", (x,y,w,h))
    # cv2.drawContours(roi, [approx], -1, (0, 255, 0), 1)
    if h > 15:
        cv2.rectangle(roi, (x, y), (x+w, y+h), (0, 255, 0), 1);

plt.subplot(223)
plt.imshow(roi)

plt.show()
