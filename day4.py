minValue = 231832
maxValue = 767346

def hasDouble(num):
    strNum = str(num)
    for i in range(len(strNum)-1):
        if strNum[i] == strNum[i+1]:
            return True
    return False

def nonDecreasing(num):
    strNum = str(num)
    for i in range(len(strNum)-1):
        if strNum[i] > strNum[i+1]:
            return False
    return True

def solve1():
    count = 0
    for num in range(minValue, maxValue +1):
        if hasDouble(num) and nonDecreasing(num):
            count += 1
    return count

print('part 1 solution:', solve1())

def hasExactlyDouble(num):
    strNum = str(num)
    for i in range(len(strNum)-1):
        # check if strNum[i] and strNum[i+1] is a matching double
        # make sure strNum[i-1] and strNum[i+2] are different than the match
        quad = ['*' if i == 0 else strNum[i-1], strNum[i], strNum[i+1], '*' if i+2 == len(strNum) else strNum[i+2]]
        digit = strNum[i]

        if (not digit == quad[0]) and (digit == quad[1]) and (digit == quad[2]) and  ( not digit == quad[3]):
            return True
    return False

def solve2():
    count = 0
    for num in range(minValue, maxValue +1):
        if hasExactlyDouble(num) and nonDecreasing(num):
            count+= 1
    return count

print('part 2: solution',solve2())