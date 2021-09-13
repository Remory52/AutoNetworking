import cv2
from numpy.lib.function_base import place
import extractor
import placer
from time import sleep

sleep(3)

image = cv2.imread("feladat.jpg")

pairs = extractor.identify(image, "templates/", 0.5)
y = placer.estimate(pairs)
h = placer.plant(pairs, y)

colors = {"pc.PNG" : (0, 0, 0), "router.PNG" : (255, 0, 0), "server.PNG" : (0, 255, 0), "switch.PNG" : (0, 0, 255)}

for ((startX, startY, endX, endY), pattern) in pairs:
    cv2.rectangle(image, (startX, startY), (endX, endY), colors[pattern], 4)

#for p in y:
    #cv2.circle(image, placer.addVectorToPoint((550, 500), p), 6, (0, 100, 255), -1)

cv2.imshow("Detection", image)
cv2.waitKey(0)