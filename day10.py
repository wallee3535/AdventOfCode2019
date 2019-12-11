from fractions import Fraction
from math import atan2, pi, sqrt
from collections import deque

class Slope:
    def __init__(self, x, y):
        self.sx = 1 if x >= 0 else -1
        self.sy = 1 if y >= 0 else -1

        if not x and not y:
            raise Exception('both zeroes')
        if not x or not y:
            if x:
                self.x = 1
                self.y = 0
            else:
                self.x = 0
                self.y = 1
        else:
            frac = Fraction(x, y)
            self.x = abs(frac.numerator)
            self.y = abs(frac.denominator)

    def __eq__(self, other):
        return (self.x, self.y, self.sx, self.sy) == (other.x, other.y, other.sx, other.sy)

    def __hash__(self):
        return hash((self.x, self.y, self.sx, self.sy))


def getMap():
    with open('./inputs/input10.txt', 'r') as fp:
        map = []
        for row in fp:
            map.append(row.strip())
        # taking transpose so x,y and map[x][y] notation works as expected
        transpose = [[] for _ in range(len(map[0]))]
        for row in map:
            for i, v in enumerate(row):
                transpose[i].append(v)

        return transpose
def getAllCoords(maxX, maxY):
    coords = []
    for i in range(maxX):
        for j in range(maxY):
            coords.append((i, j))
    return coords

def getAllAsteroidCoords(map):
    coords = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] != '#':
                continue
            coords.append((i, j))
    return coords

def getVector(src, dest):
    return tuple(a - b for a, b in zip(dest, src))

def getSlopeData(src, dest):
    dx = dest[0] - src[0]
    dy = dest[1] - src[1]
    return Slope(dx, dy)

def solve1():
    map = getMap()
    asteroidCoords = getAllAsteroidCoords(map)
    bestNumVisibleAsteroids = 0
    bestAsteroidCoord = None
    for src in asteroidCoords:
        slopesSeen = set()
        numVisibleAsteroids = 0
        for dest in asteroidCoords:
            if src == dest:
                continue
            slope = getSlopeData(src, dest)
            if slope in slopesSeen:
                continue
            else:
                slopesSeen.add(slope)
                numVisibleAsteroids += 1
        if numVisibleAsteroids > bestNumVisibleAsteroids:
            bestNumVisibleAsteroids = numVisibleAsteroids
            bestAsteroidCoord = src
    return bestAsteroidCoord, bestNumVisibleAsteroids

print('part 1 solution:', solve1())

def getCoordDistSlopes(monitoringStation, asteroidCoords):
    coordDistSlopes = []
    for coord in asteroidCoords:
        if coord == monitoringStation:
            continue
        slope = getSlopeData(monitoringStation, coord)
        dist = sqrt(sum([v ** 2 for v in [coord[0]-monitoringStation[0], coord[1]-monitoringStation[1]]]))
        coordDistSlopes.append((coord, dist, slope))
    return coordDistSlopes

def getCcwRotationFromUp(slope):
    if slope.x == 0 and slope.y == 0:
        raise Exception("cant get slope of 0,0")
    if slope.x == 0:
        return 0 if slope.sy == -1 else pi
    if slope.y == 0:
        return pi/2 if slope.sx == 1 else pi/2 + pi
    refAngle = atan2(slope.y, slope.x)
    if slope.sx >= 0 and slope.sy >= 0:
        return refAngle + pi/2
    elif slope.sx >= 0 and slope.sy < 0:
        return pi/2 - refAngle
    elif slope.sx < 0 and slope.sy < 0:
        return 3/2 *pi + refAngle
    elif slope.sx < 0 and slope.sy >= 0:
        return 3/2*pi - refAngle
    else:
        raise Exception("should not happen")

def solve2():
    map = getMap()
    asteroidCoords = getAllAsteroidCoords(map)
    monitoringStation = solve1()[0]

    coordDistSlopes = getCoordDistSlopes(monitoringStation, asteroidCoords)
    slopesSet = {slope for (_,_, slope) in coordDistSlopes}
    slopesList = list(slopesSet)
    slopesList.sort(key = getCcwRotationFromUp)
    slopeToAsteroids = {slope: [] for slope in slopesSet}
    for coordDistSlope in coordDistSlopes:
        (coord, dist, slope) = coordDistSlope
        slopeToAsteroids[slope].append(coordDistSlope)
    for slope, asteroid in slopeToAsteroids.items():
        asteroid.sort(key = lambda x: x[1], reverse = True)

    laserSlopeOrder = deque(slopesList)
    destroyedAsteroidCoords = []
    while laserSlopeOrder:
        slope = laserSlopeOrder.popleft()
        asteroids = slopeToAsteroids[slope]
        destroyedAsteroid = asteroids.pop()
        destroyedAsteroidCoords.append(destroyedAsteroid[0])
        if len(asteroids):
            laserSlopeOrder.append(slope)


    return destroyedAsteroidCoords[199]

# for coord in [(0, -5), (1,-5), (1, 0), (1,5), (0,5), (-1,5), (-1,0), (-1,-5)]:
#     print(getCcwRotationFromUp(Slope(coord[0], coord[1])) * 360 /(2*pi))

print('part 2 solution:', solve2())
