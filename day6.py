def getLocalOrbits():
    orbits = []
    with open('./inputs/input6.txt', 'r') as fp:

        for line in fp:
            # [center, orbiter] = line.split(')')
            orbit = line.strip().split(')')
            orbits.append(orbit)
    return orbits

def getOrbiterToOrbitees(orbits):
    dict = {}
    for orbit in orbits:
        orbiter = orbit[1]
        orbitee = orbit[0]
        if orbiter not in dict:
            dict[orbiter] = []
        if orbitee not in dict:
            dict[orbitee] = []
        dict[orbiter].append(orbitee)
    return dict

def getTotalOrbitsHelper(orbiter, orbiterToOrbitees, orbiterToNumOrbits):
    if orbiter in orbiterToNumOrbits:
        return orbiterToNumOrbits[orbiter]
    #direct orbits
    total = len(orbiterToOrbitees[orbiter])
    #indirect orbits
    for childOrbiter in orbiterToOrbitees[orbiter]:
        total += getTotalOrbitsHelper(childOrbiter, orbiterToOrbitees, orbiterToNumOrbits)

    orbiterToNumOrbits[orbiter] = total
    return total

def getTotalOrbits(orbiterToOrbitees):
    total = 0
    orbiterToNumOrbits = {}
    for orbiter in orbiterToOrbitees:
        total += getTotalOrbitsHelper(orbiter, orbiterToOrbitees, orbiterToNumOrbits)
    return total

def solve1():
    localOrbits = getLocalOrbits()
    print('localOrbits', localOrbits)
    orbiterToOrbitees = getOrbiterToOrbitees(localOrbits)
    res = getTotalOrbits(orbiterToOrbitees)
    return res

print('part 1 solution:', solve1())

def getUndirectedGraph(localOrbits):
    orbiterToNeighbor = {}
    for orbit in localOrbits:
        orbiter = orbit[1]
        orbitee = orbit[0]
        if orbiter not in orbiterToNeighbor:
            orbiterToNeighbor[orbiter] = []
        orbiterToNeighbor[orbiter].append(orbitee)
        if orbitee not in orbiterToNeighbor:
            orbiterToNeighbor[orbitee] = []
        orbiterToNeighbor[orbitee].append(orbiter)
    return orbiterToNeighbor

from collections import deque

def shortestPathLenth(orbiterToNeighbor, src, dest):
    visited = set()
    q = deque()
    q.append(src)
    dist = 0
    while q:
        size = len(q)
        for _ in range(size):
            orbiter = q.popleft()
            if orbiter == dest:
                return dist
            if orbiter in visited:
                continue
            visited.add(orbiter)
            for orbiterNeighbor in orbiterToNeighbor[orbiter]:
                if orbiterNeighbor not in visited:
                    q.append(orbiterNeighbor)
        dist += 1
    return dist


    pass
def solve2():
    localOrbits = getLocalOrbits()
    graph = getUndirectedGraph(localOrbits)
    dist = shortestPathLenth(graph, 'YOU', 'SAN')
    jumpsNeeded = dist -2
    return jumpsNeeded

print('part 2: solution',solve2())