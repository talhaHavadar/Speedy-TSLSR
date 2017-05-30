import cv2
import numpy as np


def __findCircles(mask):
    """
        Finds circles from mask and returns HoughCircles
    """
    circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1, 100, param1=30, param2=50)
    return circles

def __filterRedColor(image_hsv):
    """
        Filters the red color from image_hsv and returns mask.
    """
    mask1 = cv2.inRange(image_hsv, np.array([0, 100, 65]), np.array([10, 255, 255]))
    mask2 = cv2.inRange(image_hsv, np.array([155, 100, 70]), np.array([179, 255, 255]))
    mask = mask1 + mask2
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2,2)))
    mask = cv2.Canny(mask, 50, 100)
    mask = cv2.GaussianBlur(mask, (13, 13), 0)
    return mask

def __extract_sign_roi(image, circle):
    """
        @circle => (x, y, r)
        Extracts roi from image and returns the roi
    """
    x, y, r = circle
    rn = r - 5
    rect = [(x - rn), (y - rn), (x + rn), (y + rn)]
    return image[rect[1]:rect[3], rect[0]:rect[2]]

def tslsr(image):
    """
        Takes an image then returns (mask, circles, rois for each circle)
    """
    image_hsv = cv2.cvtColor(cv2.GaussianBlur(image, (7, 7), 0), cv2.COLOR_BGR2HSV)
    mask = __filterRedColor(image_hsv)
    circles = __findCircles(mask)
    rois = []
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            rois.append(__extract_sign_roi(image, (x, y, r)))

    return (mask, circles, rois)
