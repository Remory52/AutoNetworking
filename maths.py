import numpy as np

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

def pointsToRect(p1, p2):
    return (p1[0], p1[1], p2[0], p2[1])

def getDistance(p1, p2):
    (p1x, p1y) = p1
    (p2x, p2y) = p2
    x = np.power((p2x - p1x), 2) + np.power((p2y - p1y), 2)
    return round(np.sqrt(x), 2)