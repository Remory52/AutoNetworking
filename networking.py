import cv2
import numpy as np
from imutils.object_detection import non_max_suppression

image = cv2.imread("frame1.PNG")
template = cv2.resize(cv2.imread("templates/pc.PNG"), dsize=(0, 0), fx=0.5, fy=0.5)

imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
(tH, tW) = template.shape[:2]

result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)
(yCoords, xCoords) = np.where(0.6 < result)

rects = []
for (x, y) in zip(xCoords, yCoords):
	rects.append((x, y, x + tW, y + tH))

pick = non_max_suppression(np.array(rects))

print(len(pick))

for (startX, startY, endX, endY) in pick:
	# draw the bounding box on the image
	cv2.rectangle(image, (startX, startY), (endX, endY), (255, 0, 0), 3)

# show the output image
cv2.imshow("Output", cv2.resize(image, dsize=(0, 0), fx=0.8, fy=0.8))
cv2.waitKey(0)