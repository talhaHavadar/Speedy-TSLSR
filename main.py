import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("../images/speed-3.jpg", 1)

blur = cv2.GaussianBlur(image, (7, 7), 0)
image_hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
mask1 = cv2.inRange(image_hsv, np.array([0, 100, 65]), np.array([10, 255, 255]))
mask2 = cv2.inRange(image_hsv, np.array([155, 100, 70]), np.array([179, 255, 255]))
mask = mask1 + mask2
mask = cv2.dilate(mask, (7, 7), iterations=5)
# mask = cv2.erode(mask, (5, 5), iterations=1)
mask = cv2.Canny(mask, 50, 100)
mask = cv2.GaussianBlur(mask, (13, 13), 0)
# mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, (13, 13))

plt.figure(1)
plt.imshow(image_hsv, cmap="hsv")

plt.figure(3)
plt.imshow(mask, cmap="gray")

circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1, 100, param1=30, param2=50)
print(circles)
# ensure at least some circles were found
if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype("int")

	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv2.circle(image, (x, y), r, (0, 255, 0), 2)
		cv2.rectangle(image, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

plt.figure(2)
plt.imshow(image)
plt.show()
