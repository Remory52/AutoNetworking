import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
from imutils.object_detection import non_max_suppression
import maths

def identify(image, templateDir, threshold=0.5):    
    boxes = []
    pair = []
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    templates = [f for f in listdir(templateDir) if isfile(join(templateDir, f))]

    for template in templates:
        templateGray = cv2.resize(cv2.imread(templateDir + template, cv2.IMREAD_GRAYSCALE), dsize=(0, 0), fx=0.3, fy=0.3)
        (tH, tW) = templateGray.shape[:2]

        result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)
        (ys, xs) = np.where(threshold < result)

        rects = []
        for (x, y) in zip(xs, ys):
            rects.append((x, y, x + tW, y + tH))

        filtered = non_max_suppression(np.array(rects))
        
        for x in filtered:
            boxes.append(x)
            pair.append((x, template))

    recognitions = non_max_suppression(np.array(boxes))
    tmp = pair.copy()

    removedCount = 0
    for i in range(0, len(pair)):
        (box, template) = pair[i]

        if(box not in recognitions):
            tmp.pop(i - removedCount)
            removedCount += 1

    recognitionCenters = [maths.getCenter(x[0]) for x in tmp]
    dist = []
    overlapping = [] #store indexes of overlapping boxes

    for ii in range(0, len(tmp)):
        (box, template) = tmp[ii]
        if(template == "pc.PNG" or template == "server.PNG"):
            continue

        boxCenter = maths.getCenter(box)
        dist = [maths.getDistance(boxCenter, x) for x in recognitionCenters]

        collisionID = [i for i in range(len(dist)) if dist[i] == 1]

        if len(collisionID) == 1:
            overlapping.append(collisionID[0])
        
    if 1 <= len(overlapping):
        for ovI in overlapping:
            del tmp[ovI]

    return tmp