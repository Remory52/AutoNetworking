from pyautogui import position
import maths
import numpy as np

pcRule = {"max_conn" : 1, "primary_conn" : "switch.PNG"}
serverRule = {"max_conn" : 1, "primary_conn" : "switch.PNG"}
switchRule = {"max_conn" : 5, "primary_conn" : "router.PNG"}
routerRule = {"max_conn" : 5, "primary_conn" : "router.PNG"}

rules = {"pc.PNG" : pcRule, "server.PNG" : serverRule, "switch.PNG" : switchRule, "router.PNG" : routerRule}

def makeNet(pairs):
    nets = []
    for (pos, device) in pairs:
        string = []

        string.append((tuple(pos), device))
        for (inPos, innerDev) in pairs:
           if rules[device]["primary_conn"] == innerDev:
               string.append((tuple(inPos), innerDev))
        nets.append(string)

    return nets

def weave(nets):
    selected = []
    for net in nets:
        starterDevice = net[0]
        starterPosition = maths.getCenter(tuple(starterDevice[0]))
        
        distances = []
        for (endPosition, endDevice) in net[1:]:
            distances.append(maths.getDistance(starterPosition, maths.getCenter(endPosition)))

        closestIndex = distances.index(min(distances))
        closestDevice = net[closestIndex + 1]
        #print(starterDevice[1], distances, maths.getCenter(closestDevice[0]))
        selected.append((starterDevice, closestDevice))

    return selected