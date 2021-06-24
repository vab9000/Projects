import random


def add_point(terrainPoints):
    lastPlacedPoint = terrainPoints[-2]
    addRandom = random.randint(-1, 1)
    if lastPlacedPoint[1] > 460:
        addRandom = random.randint(-1, 0)
    elif lastPlacedPoint[1] < 120:
        addRandom = random.randint(0, 5)
    listToAppend = [lastPlacedPoint[0] + 5, lastPlacedPoint[1] + addRandom]
    terrainPoints.insert(-1, listToAppend)
    return terrainPoints


def remove_point(terrainPoints):
    terrainPoints.pop(1)
    for point in terrainPoints[1:-1]:
        point[0] -= 5
    return terrainPoints
