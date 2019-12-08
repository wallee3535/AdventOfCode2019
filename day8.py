def getLayers():
    layers = []
    with open('./inputs/input8.txt', 'r') as fp:
        input = fp.read()
        for i in range(0, len(input), 25*6):
            layer = input[i: i+ (25*6)]
            layers.append(layer)
    return layers

def solve1():
    layers = getLayers()
    zeroCounts = [layer.count('0') for layer in layers]
    minIndex = zeroCounts.index(min(zeroCounts))
    minLayer = layers[minIndex]

    return minLayer.count('1') * minLayer.count('2')
print('part 1 solution:', solve1())

def overlay(layers):
    finalLayer = []
    for pixelIndex in range(25 * 6):
        finalColor = '2'
        for layer in layers:
            color = layer[pixelIndex]
            if color == '0' or color == '1':
                finalColor = color
                break
        finalLayer.append(finalColor)
    return finalLayer

def layerToMatrix(layer):
    matrix = []
    for r in range(6):
        matrix.append(layer[r*25:r*25+25])
    return matrix

def printReadableMatrix(matrix):
    for row in matrix:
        print("".join(row).replace('0', '-').replace('1', '|'))

def solve2():
    layers = getLayers()
    finalLayer = overlay(layers)
    matrix = layerToMatrix(finalLayer)
    printReadableMatrix(matrix)

print('part 2: solution',solve2())