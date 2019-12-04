from functools import reduce

def getLines():
    wires = []
    with open('./inputs/input3.txt', 'r') as fp:
        for line in fp:
            wire = line.split(',')
            wires.append(wire)

    return wires

def moveToVector(move):
    dir = move[0]
    mag = int(move[1:])
    charToVector = {'R':[1,0], 'L':[-1,0], 'U': [0,1], 'D': [0,-1]}
    unitVector = charToVector[dir]
    vector = [ mag * v for v in unitVector]
    return vector

def getPoints(wire):
    points = []
    pos = [0,0]
    points.append(pos)
    for move in wire:
        vector = moveToVector(move)
        pos = [pos[0] + vector[0], pos[1] + vector[1]]
        points.append(pos)
    return points

def getManhattanDistance(a1, a2):
    return abs(a1[0]-a2[0]) + abs(a1[1]-a2[1])
def pointsToVector(a, b):
    return [b[0]-a[0], b[1]-a[1]]
def dotProd(a, b):
    return a[0]*b[0] + a[1] * b[1]
def between(a, b, m):
    # return (a[0] <= m[0] <= b[0]) and  (a[1] <= m[1] <= b[1])
    return getManhattanDistance(a, b) == getManhattanDistance(a, m) + getManhattanDistance(b, m)
def getIntersection(a1, a2, b1, b2):
    va = pointsToVector(a1, a2)
    vb = pointsToVector(b1, b2)
    intersection = []
    if dotProd(va, vb) == 0:
        if a1[0] == a2[0]:
            # a is vertical
            intersection = [a1[0], b1[1]]
        else:
            # a is horizontal
            intersection = [b1[0], a1[1]]
        if between(a1, a2, intersection) and between(b1, b2, intersection):
            return intersection
        else:
            return None
    else:
        return None





def getIntersections(points0, points1):
    intersections = []
    for i in range(len(points0) -1):
        for j in range(len(points1) -1):
            intersection = getIntersection(points0[i], points0[i+1], points1[j], points1[j+1])
            if intersection:
                intersections.append(intersection)
    return intersections



def getClosest(origin, points):
    points = points[1:]
    closestPoint = points[0]
    closestDist = getManhattanDistance(origin, points[0])
    for point in points:
        dist = getManhattanDistance(origin, point)
        if dist < closestDist:
            closestDist = dist
            closestPoint = point
    return closestPoint

def solve1():

    wires = getLines()
    points0 = getPoints(wires[0])
    print('points0', points0)

    points1 = getPoints(wires[1])
    print('points1', points1)
    intersections = getIntersections(points0, points1)
    print(intersections)
    closestPoint = getClosest([0,0], intersections)
    dist = getManhattanDistance([0, 0], closestPoint)
    return dist


print('testing', getIntersection([146, 4], [217, 4], [155, 46], [155, -12]))





print('part 1 solution:', solve1())

def getIntersectionData(points0, points1):
    coords = []
    for i in range(len(points0) -1):
        for j in range(len(points1) -1):
            intersection = getIntersection(points0[i], points0[i+1], points1[j], points1[j+1])
            if intersection:
                coords.append([i,j, intersection])
    return coords

def getCummulativeDists(points):
    dists = []
    curDist = 0
    prev = [0,0]
    for point in points:
        dist = getManhattanDistance(prev, point)
        curDist += dist
        dists.append(curDist)
        prev = point
    return dists

def solve2():
    wires = getLines()
    points0 = getPoints(wires[0])
    points1 = getPoints(wires[1])
    intersectionData = getIntersectionData(points0, points1)
    cumDists0 = getCummulativeDists(points0)
    cumDists1 = getCummulativeDists(points1)
    intersectionDists = []
    for intersection in intersectionData:
        i = intersection[0]
        j = intersection[1]
        coord = intersection[2]
        dist= cumDists0[i] + cumDists1[j] + getManhattanDistance(coord, points0[i]) + getManhattanDistance(coord, points1[j])
        intersectionDists.append(dist)
    shortestDist = min([d for d in intersectionDists if d > 0])
    print('intersectionDists', intersectionDists)
    return shortestDist



print('part 2: solution',solve2())