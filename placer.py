import pyautogui
import cv2
import numpy as np

end_device = (50, 950)
pc = (230, 950)
server = (300, 950)

network_device = (20, 950)
routers = (20, 1020)
switches = (50, 1020)
PT_router = (600, 950)
switch2960 = (230, 950)

def plant(starting, pairs, places):
    pass

def estimate(pairs):
    positions = np.array(pairs, dtype=object)[0:len(pairs), 0:1]
    top = [x[0][1] for x in positions]

    rootIndex = top.index(min(top))
    root = positions[rootIndex]

    rootCenter = getCenter(root[0])
    places = []
    for rects in positions:
        (vx, vy) = vectorHeading(rootCenter, getCenter(rects[0]))
        places.append((vx, vy))

    #poses.remove(rootCenter)
    #poses.insert(0, rootCenter)

    return places

def getCenter(rect):
    (startX, startY, endX, endY) = rect
    center = (int(startX + ((endX - startX) / 2)), (int(endY - ((endY - startY) / 2))))
    return center

def vectorHeading(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    vx = int(x2 - x1)
    vy = int(y2 - y1)
    return (vx, vy)

def addVectorToPoint(vector, point):
    return tuple(map(lambda a, b: a + b, vector, point))
