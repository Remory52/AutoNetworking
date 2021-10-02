import cv2
from numpy.lib.function_base import place
import extractor
import placer
from time import sleep
import spider
import maths

#sleep(3)

image = cv2.imread("examples/feladat.jpg")
#image = cv2.resize(cv2.imread("examples/feladat1.jpg"), (0, 0), fx=1.4, fy=1.4)

pairs = extractor.identify(image, "templates/", 0.5)
places = placer.estimate(pairs)
#placer.plant(pairs, places)
nets = spider.makeDevicePairs(pairs)
selected = spider.weave(nets)

colors = {"pc.PNG" : (0, 0, 0), "router.PNG" : (255, 0, 0), "server.PNG" : (0, 255, 0), "switch.PNG" : (0, 0, 255)}

for ((startX, startY, endX, endY), pattern) in pairs:
    cv2.rectangle(image, (startX, startY), (endX, endY), colors[pattern], 2)

for select in selected:
    k = select
    #startX, startY, endX, endY = k[0][0]
    #cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 4)

    p1 =  maths.getCenter(select[0][0])
    p2 =  maths.getCenter(select[1][0])
    distance = maths.getDistance(p1, p2)
    lineCent = maths.getCenter(maths.pointsToRect(p1, p2))
    cv2.putText(image, str(distance), (p1[0], p1[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, ), 1, cv2.LINE_AA)
    cv2.line(image, p1, p2, (0, 0, 255), 2, cv2.LINE_AA)

    #startX, startY, endX, endY = k[1][0]
    #cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 4)

cv2.imshow("Detection", image)
cv2.waitKey(0)