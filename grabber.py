import cv2
import numpy as np
import random as rnd
from os import listdir
from os.path import isfile, join
from imutils.object_detection import non_max_suppression

colors = {"pc.PNG" : (0, 0, 0), "router.PNG" : (255, 0, 0), "server.PNG" : (0, 255, 0), "switch.PNG" : (0, 0, 255)}

templateDir = "templates/"
templates = [f for f in listdir(templateDir) if isfile(join(templateDir, f))]
image = cv2.imread("frame1.PNG")
thres = 0.5

imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

boxes = []
pair = []

for template in templates:
    templateGray = cv2.resize(cv2.imread(templateDir + template, cv2.IMREAD_GRAYSCALE), dsize=(0, 0), fx=0.3, fy=0.3)
    (tH, tW) = templateGray.shape[:2]

    result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)
    (ys, xs) = np.where(thres < result)

    rects = []
    for (x, y) in zip(xs, ys):
        rects.append((x, y, x + tW, y + tH))

    filtered = non_max_suppression(np.array(rects))
    
    for x in filtered:
        boxes.append(x)
        pair.append((x, template))

    color = (rnd.randint(0, 255), 0, rnd.randint(0, 255))

recognitions = non_max_suppression(np.array(boxes))
tmp = pair.copy()

removedCount = 0
for i in range(0, len(pair)):
    (box, template) = pair[i]

    if(box not in recognitions):
        tmp.pop(i - removedCount)
        removedCount += 1

pair = tmp.copy()

for ((startX, startY, endX, endY), pattern) in pair:
    cv2.rectangle(image, (startX, startY), (endX, endY), colors[pattern], 4)

cv2.imshow("Recognition", cv2.resize(image, dsize=(0, 0), fx=0.5, fy=0.5))
cv2.waitKey(0)