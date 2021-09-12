import pyautogui
import cv2
import numpy as np

def plant():
    pass

def estimate(pairs):
    positions = np.array(pairs, dtype=object)[0:-1, 0:1]
    top = []
    for x in positions:
        top.append(x[0][1])

    rootIndex = top.index(min(top))
    root = positions[rootIndex]

    #positions = np.delete(positions, rootIndex)

    rootCenter = getCenter(root[0])
    poses = []
    for rects in positions:
        pos = addVectorToPoint(vectorHeading(rootCenter, getCenter(rects[0])), rootCenter)
        poses.append(pos)

    return poses

def getCenter(rect):
    (startX, startY, endX, endY) = rect
    center = (int(startX + ((endX - startX) / 2)), (int(endY - ((endY - startY) / 2))))
    return center

def vectorHeading(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    x = int((x2 - x1) / 2)
    y = int((y2 - y1) / 2)
    return (x, y)

def addVectorToPoint(vector, point):
    return tuple(map(lambda a, b: a + b, vector, point))
