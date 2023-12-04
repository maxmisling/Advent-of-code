from functools import reduce
input = open("Day3Input.txt").read().strip()
lines = input.split('\n')

nums_matrix = [[0 for j in range(len(lines[0]))] for i in range(len(lines))]
nums_and_index = []
gear_index = []

for i, line in enumerate(lines):
    num = ""
    start_j = 0
    for j, c in enumerate(line):
        if c.isdigit():
            if not num:
                start_j = j
            num += c
        else:
            if num:
                nums_and_index.append((num, i, start_j))
                for x in range(start_j, start_j + len(num)):
                    nums_matrix[i][x] = int(num)
            num = ""
            if c == '*':
                gear_index.append((i, j))
    if num:
        nums_and_index.append([num, i, start_j])
        for x in range(start_j, start_j + len(num)):
            nums_matrix[i][x] = int(num)

def isNumValid(r, c, size):
   for i in range(r-1, r+2):
       for j in range(c-1, c+size+1):
           if i < 0 or i >= len(lines) or j < 0 or j >= len(lines[0]):
                continue
           if lines[i][j] != '.' and not lines[i][j].isdigit():
               return True
   return False

part1 = 0
for numbers in nums_and_index:
    if isNumValid(numbers[1], numbers[2], len(numbers[0])):
        part1 += int(numbers[0])

def getAdjacentNums(r, c):
    nums = set()
    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            if i < 0 or i >= len(lines) or j < 0 or j >= len(lines[0]):
                continue
            if nums_matrix[i][j] != 0:
                nums.add(nums_matrix[i][j])
    return list(nums)

part2 = 0
for gear in gear_index:
    adjacent_nums = getAdjacentNums(gear[0], gear[1])
    if len(adjacent_nums) == 2:
        part2 += adjacent_nums[0] * adjacent_nums[1]

print(part1)
print(part2)