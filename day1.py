def solve1():
    fuel = 0

    with open('./inputs/input1.txt', 'r') as fp:
        for line in fp:
            mass = int(line)
            fuel += mass//3 - 2

    return fuel

print('part 1 solution:', solve1())

def getFuel(mass):
    return mass//3 -2

def solve2():
    totalFuel = 0

    with open('./inputs/input1.txt', 'r') as fp:
        for line in fp:
            moduleFuel = 0
            mass = int(line)
            currentFuel = getFuel(mass)
            while currentFuel > 0:
                moduleFuel += currentFuel
                currentFuel = getFuel(currentFuel)

            totalFuel += moduleFuel
    return totalFuel

print('part 2: solution',solve2())

