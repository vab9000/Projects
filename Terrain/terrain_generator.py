import random

def add_point(points, distance, length, mini, maxi):
    lastPlacedPoint = points[-2]
    addRandom = random.randint(-distance, distance)
    if lastPlacedPoint[1] > maxi:
        addRandom = random.randint(-distance, 0)
    elif lastPlacedPoint[1] < mini:
        addRandom = random.randint(0, distance)
    listToAppend = [lastPlacedPoint[0] + distance, lastPlacedPoint[1] + addRandom]
    points.insert(-1, listToAppend)
    return points


def remove_point(points, distance):
    points.pop(1)
    for point in points[1:-1]:
        point[0] -= distance
    return points
