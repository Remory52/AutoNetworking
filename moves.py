from time import sleep
import cv2
import pyautogui

image = cv2.imread("frame1.PNG")

sleep(3)

end_device = (50, 950)
pc = (230, 950)
server = (300, 950)

network_device = (20, 950)
routers = (20, 1020)
switches = (50, 1020)
PT_router = (600, 950)
switch2960 = (230, 950)

#place router
router = [network_device, routers, PT_router]

for (x, y) in router:
    pyautogui.click(x, y)

pyautogui.click(500, 500)

#for (x, y) in poses:
#    cv2.circle(image, (x, y), 5, (0, 0, 255), -1)

cv2.imshow("recog", cv2.resize(image, (0, 0), fx=0.8, fy=0.8))
cv2.waitKey(0)