import cv2
import numpy as np
from numpy.core.fromnumeric import shape

class Sieve:

    def sieve(image):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        hsv = cv2.GaussianBlur(hsv, (21, 21), 10)

        lower_range = np.array([1,1,1])
        upper_range = np.array([254,254,254])

        mask = cv2.inRange(hsv, lower_range, upper_range)
        result = cv2.bitwise_and(image, image, mask=mask)
        
        return result

    def wash(image):
        for y in range(0, image.shape[:2][0]):
            for x in range(0, image.shape[:2][1]):
                r, g, b = image[y, x]

                if(0 <= r <= 50 and 0 <= g <= 50 and 0 <= b <= 50):
                    image[y, x] = [255, 255, 255]

        return image
       