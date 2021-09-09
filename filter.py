import cv2
import numpy as np

@staticmethod
def filter(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv = cv2.GaussianBlur(hsv, (21, 21), 10)

    lower_range = np.array([1,1,1])
    upper_range = np.array([254,254,254])

    mask = cv2.inRange(hsv, lower_range, upper_range)
    result = cv2.bitwise_and(image, image, mask=mask)
    
    return result