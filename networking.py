import pyautogui
import cv2
import numpy as np

screenshot = pyautogui.screenshot()
image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

cv2.imshow("cicc", image)
cv2.waitKey()