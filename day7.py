from threading import Thread, Lock
import time
from  queue import Queue


class AmplifierThread(Thread):
    def __init__(self, name, nums, inputQueue, outputQueue):
        super().__init__()
        self.name = name
        self.nums = nums
        self.inputQueue = inputQueue
        self.outputQueue = outputQueue

    def run(self):
        nums = self.nums
        outputs = []
        i = 0
        while i < len(nums):
            # print(self.name, 'i:', i, flush=True)
            num = nums[i]

            opcode = num % 100
            num //= 100
            mode1 = num % 10
            num //= 10
            mode2 = num % 10
            num //= 10
            mode3 = num % 10

            if opcode == 1:
                val1 = nums[nums[i + 1]] if mode1 == 0 else nums[i + 1]
                val2 = nums[nums[i + 2]] if mode2 == 0 else nums[i + 2]
                val3 = nums[i + 3]
                total = val1 + val2
                nums[val3] = total
                i += 4
            elif opcode == 2:
                val1 = nums[nums[i + 1]] if mode1 == 0 else nums[i + 1]
                val2 = nums[nums[i + 2]] if mode2 == 0 else nums[i + 2]
                val3 = nums[i + 3]
                product = val1 * val2
                nums[val3] = product
                i += 4
            elif opcode == 3:
                val1 = nums[i + 1]
                # print(self.name, 'getting input...', flush=True)
                inputVal = self.inputQueue.get(block=True)
                # print(self.name, 'input:', inputVal, flush=True)
                nums[val1] = inputVal

                i += 2
            elif opcode == 4:
                val1 = nums[nums[i + 1]] if mode1 == 0 else nums[i + 1]
                # print(self.name, 'output:', val1, flush=True)
                self.outputQueue.put(val1, block=True)
                i += 2
            elif opcode == 5:
                val1 = nums[nums[i + 1]] if mode1 == 0 else nums[i + 1]
                val2 = nums[nums[i + 2]] if mode2 == 0 else nums[i + 2]
                if val1 != 0:
                    i = val2
                else:
                    i += 3
            elif opcode == 6:
                val1 = nums[nums[i + 1]] if mode1 == 0 else nums[i + 1]
                val2 = nums[nums[i + 2]] if mode2 == 0 else nums[i + 2]
                if val1 == 0:
                    i = val2
                else:
                    i += 3
            elif opcode == 7:
                val1 = nums[nums[i + 1]] if mode1 == 0 else nums[i + 1]
                val2 = nums[nums[i + 2]] if mode2 == 0 else nums[i + 2]
                val3 = nums[i + 3]
                if val1 < val2:
                    nums[val3] = 1
                else:
                    nums[val3] = 0
                i += 4
            elif opcode == 8:
                val1 = nums[nums[i + 1]] if mode1 == 0 else nums[i + 1]
                val2 = nums[nums[i + 2]] if mode2 == 0 else nums[i + 2]
                val3 = nums[i + 3]
                if val1 == val2:
                    nums[val3] = 1
                else:
                    nums[val3] = 0
                i += 4

            elif opcode == 99:
                # print(self.name, 'terminated.', flush=True)
                break
            else:
                raise Exception('uknown op')

def getNums():
    with open('./inputs/input7.txt', 'r') as fp:
        data = fp.read()
        strNums = data.split(',')
        nums = [int(s) for s in strNums]
        return nums


def getThrusterSignal(nums, phaseSettings):
    numAmplifiers = len(phaseSettings)
    inputQueues = [Queue() for _ in range(numAmplifiers + 1)]
    for inputQueue, phaseSetting in zip(inputQueues, phaseSettings):
        inputQueue.put(phaseSetting)
    inputQueues[0].put(0)

    locks = [Lock() for _ in range(numAmplifiers + 1)]

    amps = [AmplifierThread('Amplifier ' + str(i), nums.copy(), inputQueues[i], inputQueues[i + 1]) for i in
            range(numAmplifiers)]

    for amp in amps:
        amp.start()
        amp.join()

    return inputQueues[-1].get()

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def getAllPermutationsHelper(arr, start, res):
    if start == len(arr):
        res.append(arr.copy())
    for i in range(start, len(arr)):
        swap(arr, start, i)
        getAllPermutationsHelper(arr, start + 1, res)
        swap(arr, start, i)


def getAllPermutations(arr):
    res = []
    getAllPermutationsHelper(arr, 0, res)
    return res

def getThrusterSignalWithLoop(nums, phaseSettings):
    numAmplifiers = len(phaseSettings)
    inputQueues = [Queue() for _ in range(numAmplifiers)]
    for inputQueue, phaseSetting in zip(inputQueues, phaseSettings):
        inputQueue.put(phaseSetting)
    inputQueues[0].put(0)

    locks = [Lock() for _ in range(numAmplifiers)]

    amps = [AmplifierThread('Amplifier ' + str(i), nums.copy(), inputQueues[i], inputQueues[(i + 1) % numAmplifiers]) for i in range(numAmplifiers)]

    for amp in amps:
        amp.start()
    for amp in amps:
        amp.join()
        # print('JOINED..................', flush=True)
    res =inputQueues[0].get()

    return res


def solve1():
    nums = getNums()

    perms = getAllPermutations([0, 1, 2, 3, 4])
    thrusterSignals = [getThrusterSignal(nums, phaseSettings) for phaseSettings in perms]
    return max(thrusterSignals)

def solve2():
    nums = getNums()

    perms = getAllPermutations([9, 8, 7, 6, 5])
    thrusterSignals = [getThrusterSignalWithLoop(nums, phaseSettings) for phaseSettings in perms]
    return max(thrusterSignals)

startTime = time.clock()
print('part 1 solution:', solve1())
print('part 2: solution',solve2())
endTime = time.clock()
print('time:', endTime - startTime)
