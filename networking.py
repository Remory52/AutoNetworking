import cv2
from numpy.lib.function_base import place
import extractor
import placer
from time import sleep
import spider

#sleep(3)

image = cv2.imread("examples/feladat.jpg")
#image = cv2.resize(cv2.imread("lab2.jpg"), (0, 0), fx=0.4, fy=0.4)

pairs = extractor.identify(image, "templates/", 0.5)
places = placer.estimate(pairs)
#placer.plant(pairs, places)
nets = spider.makeNet(pairs)
selected = spider.weave(nets)

colors = {"pc.PNG" : (0, 0, 0), "router.PNG" : (255, 0, 0), "server.PNG" : (0, 255, 0), "switch.PNG" : (0, 0, 255)}

#for ((startX, startY, endX, endY), pattern) in pairs:
#    cv2.rectangle(image, (startX, startY), (endX, endY), colors[pattern], 4)

for select in selected[:3]:
    k = select
    startX, startY, endX, endY = k[0][0]
    cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 4)

    startX, startY, endX, endY = k[1][0]
    cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 4)

#for p in places:
    #cv2.circle(image, placer.addVectorToPoint((550, 500), p), 6, (0, 100, 255), -1)

cv2.imshow("Detection", image)
cv2.waitKey(0)