

def run(nums, input):
    outputs = []
    i = 0
    while i < len(nums):
        num = nums[i]

        opcode = num%100
        num //= 100
        mode1 = num%10
        num //= 10
        mode2 = num%10
        num //= 10
        mode3 = num % 10

        if opcode == 1:
            val1 = nums[nums[i+1]] if mode1 == 0 else nums[i+1]
            val2 = nums[nums[i+2]] if mode2 == 0 else nums[i+2]
            val3 = nums[i+3]
            total = val1 + val2
            nums[val3] = total
            i += 4
        elif opcode == 2:
            val1 = nums[nums[i+1]] if mode1 == 0 else nums[i+1]
            val2 = nums[nums[i+2]] if mode2 == 0 else nums[i+2]
            val3 = nums[i+3]
            product = val1 * val2
            nums[val3] = product
            i += 4
        elif opcode == 3:
            val1 = nums[i+1]
            nums[val1] = input
            i += 2
        elif opcode == 4:
            val1 = nums[nums[i+1]] if mode1 == 0 else nums[i+1]
            outputs.append(val1)
            i += 2
        elif opcode == 5:
            val1 = nums[nums[i+1]] if mode1 == 0 else nums[i+1]
            val2 = nums[nums[i + 2]] if mode2 == 0 else nums[i + 2]
            if val1 != 0:
                i = val2
            else:
                i += 3
        elif opcode == 6:
            val1 = nums[nums[i+1]] if mode1 == 0 else nums[i+1]
            val2 = nums[nums[i + 2]] if mode2 == 0 else nums[i + 2]
            if val1 == 0:
                i = val2
            else:
                i += 3
        elif opcode == 7:
            val1 = nums[nums[i+1]] if mode1 == 0 else nums[i+1]
            val2 = nums[nums[i + 2]] if mode2 == 0 else nums[i + 2]
            val3 = nums[i + 3]
            if val1 < val2:
                nums[val3] = 1
            else:
                nums[val3] = 0
            i += 4
        elif opcode == 8:
            val1 = nums[nums[i+1]] if mode1 == 0 else nums[i+1]
            val2 = nums[nums[i + 2]] if mode2 == 0 else nums[i + 2]
            val3 = nums[i + 3]
            if val1 == val2:
                nums[val3] = 1
            else:
                nums[val3] = 0
            i += 4

        elif opcode == 99:
            break
        else:
            raise Exception('uknown op')
    return outputs

def getNums():
    with open('./inputs/input5.txt', 'r') as fp:
        data = fp.read()
        strNums = data.split(',')
        nums = [int(s) for s in strNums]
        return nums

def solve1():
    nums = getNums()
    try:
        outputs = run(nums, 1)
        return outputs
    except IndexError:
        print('index ERROR..........')

print('part 1 solution:', solve1())

def solve2():
    nums = getNums()
    try:
        outputs = run(nums, 5)
        return outputs
    except IndexError:
        print('index ERROR..........')

print('part 2: solution',solve2())