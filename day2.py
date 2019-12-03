def run(nums):
    i = 0
    while not nums[i] == 99:
        op = nums[i]
        a = nums[i + 1]
        b = nums[i + 2]
        c = nums[i + 3]
        if op == 1:
            nums[c] = nums[a] + nums[b]
        elif op == 2:
            nums[c] = nums[a] * nums[b]
        else:
            raise Exception('uknown op')
        i += 4

    return nums[0]

def getNums():
    with open('./inputs/input2.txt', 'r') as fp:
        data = fp.read()
        strNums = data.split(',')
        nums = [int(s) for s in strNums]
        return nums

def solve1():
    nums = getNums()

    nums[1] = 12
    nums[2] = 2

    return run(nums)


print('part 1 solution:', solve1())

def solve2():
    nums = getNums()
    for noun in range(0, 100):
        for verb in range(0, 100):
            numsCopy = nums.copy()
            numsCopy[1] = noun
            numsCopy[2] = verb
            res = run(numsCopy)
            if res == 19690720:
                return 100 * noun + verb

print('part 2: solution',solve2())