class Program:
    def __init__(self, numsList):
        self.nums = {i: v for i, v in enumerate(numsList)}
        self.relBase = 0

    def getNum(self, index, mode=1):
        """
        :param index: index to read at
        :param mode: 0 for position mode, 1 for immediate mode, 2 for relative mode
        :return: the value to use when operation operated on specified index
        """
        if mode == 0:
            return self.getNum(self.getNum(index))
        elif mode == 1:
            # this is also the base case, use 0 for default
            return self.nums.get(index, 0)
        elif mode == 2:
            return self.getNum(self.relBase + self.getNum(index))
        else:
            raise Exception('uknown mode', mode)

    def setNum(self, index, value, mode):
        if mode == 0:
            self.nums[index] = value
        elif mode == 2:
            self.nums[index + self.relBase] = value
        else:
            raise Exception('uknown mode', mode)

    def run(self, input):
        nums = self.nums
        getNum = self.getNum
        setNum = self.setNum
        outputs = []
        i = 0
        while i < len(nums):
            num = nums[i]

            opcode = num % 100
            num //= 100
            mode1 = num % 10
            num //= 10
            mode2 = num % 10
            num //= 10
            mode3 = num % 10
            modes = [mode1, mode2, mode3]

            if opcode == 1:
                val1 = getNum(i + 1, mode1)
                val2 = getNum(i + 2, mode2)
                val3 = getNum(i + 3)
                total = val1 + val2

                setNum(val3, total, mode3)
                i += 4
            elif opcode == 2:
                val1 = getNum(i + 1, mode1)
                val2 = getNum(i + 2, mode2)
                val3 = getNum(i + 3)
                product = val1 * val2

                setNum(val3, product, mode3)
                i += 4
            elif opcode == 3:
                val1 = getNum(i + 1)
                setNum(val1, input, mode1)
                i += 2
            elif opcode == 4:
                val1 = getNum(i + 1, mode1)
                outputs.append(val1)
                i += 2
            elif opcode == 5:
                val1 = getNum(i + 1, mode1)
                val2 = getNum(i + 2, mode2)
                if val1 != 0:
                    i = val2
                else:
                    i += 3
            elif opcode == 6:
                val1 = getNum(i + 1, mode1)
                val2 = getNum(i + 2, mode2)
                if val1 == 0:
                    i = val2
                else:
                    i += 3
            elif opcode == 7:
                val1 = getNum(i + 1, mode1)
                val2 = getNum(i + 2, mode2)
                val3 = getNum(i + 3)
                if val1 < val2:
                    setNum(val3, 1, mode3)
                else:
                    setNum(val3, 0, mode3)
                i += 4
            elif opcode == 8:
                val1 = getNum(i + 1, mode1)
                val2 = getNum(i + 2, mode2)
                val3 = getNum(i + 3)
                if val1 == val2:
                    setNum(val3, 1, mode3)
                else:
                    setNum(val3, 0, mode3)
                i += 4
            elif opcode == 9:
                val1 = getNum(i + 1, mode1)
                self.relBase += val1
                i += 2

            elif opcode == 99:
                break
            else:
                raise Exception('uknown op: ' + str(opcode))
        return outputs


def getNums():
    with open('./inputs/input9.txt', 'r') as fp:
        data = fp.read()
        strNums = data.split(',')
        nums = [int(s) for s in strNums]
        return nums

def solve1():
    nums = getNums()
    program = Program(nums)
    try:
        outputs = program.run(1)
        return outputs
    except IndexError:
        print('index ERROR..........')

print('part 1 solution:', solve1())

def solve2():
    nums = getNums()
    program = Program(nums)
    try:
        outputs = program.run(2)
        return outputs
    except IndexError:
        print('index ERROR..........')

print('part 2: solution',solve2())
