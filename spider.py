from pyautogui import position
import maths
import numpy as np

pcRule = {"max_conn" : 1, "primary_conn" : "switch.PNG"}
serverRule = {"max_conn" : 1, "primary_conn" : "switch.PNG"}
switchRule = {"max_conn" : 5, "primary_conn" : "router.PNG"}
routerRule = {"max_conn" : 5, "primary_conn" : "router.PNG"}

rules = {"pc.PNG" : pcRule, "server.PNG" : serverRule, "switch.PNG" : switchRule, "router.PNG" : routerRule}

def makeDevicePairs(pairs):
    """

    """
    devicePairs = []
    for (pos, device) in pairs:
        string = []

        string.append((tuple(pos), device))
        for (inPos, innerDev) in pairs:
           if rules[device]["primary_conn"] == innerDev:
               string.append((tuple(inPos), innerDev))
        devicePairs.append(string)

        #Example devicePair: [((332, 374, 374, 410), 'pc.PNG'), ((133, 265, 179, 290), 'switch.PNG'), ...]
        #Starter device position, and class | End devices positions and classes

    return devicePairs

def weave(devicePairs):
    """
    
    """
    routers = [x[0] for x in devicePairs if x[0][1] == "router.PNG"]
    
    selected = []
    for devicePair in devicePairs:
        starterDevice = devicePair[0]
        if starterDevice[1] == "router.PNG":
            continue

        starterPosition = maths.getCenter(tuple(starterDevice[0]))
       
        distances = []
        for (endPosition, endDevice) in devicePair[1:]:
            distances.append(maths.getDistance(starterPosition, maths.getCenter(endPosition)))

        #if starterDevice[1] == "router.PNG":
        #    distances[distances.index(min(distances))] = np.Infinity

        closestIndex = distances.index(min(distances))
        closestDevice = devicePair[closestIndex + 1]
        selected.append((starterDevice, closestDevice))

    return selected